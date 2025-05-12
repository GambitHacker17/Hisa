# meta developer: @MartyyyK

import time
import random
from .. import loader, utils
from telethon.utils import get_display_name

class RPSgameMod(loader.Module):
    """Game «rock, paper, scissors» in Telegram"""
    
    strings = {
        "name": "RPSgame",
        "searching": "<b>✌️ The game «Rock, Paper, Scissors»</b>",
        "join_game": "👾 Join the game",
        "game_started": "⚠ The game has already started",
        "game_already_running": "<emoji document_id=5255772095958229697>🤚</emoji> <b>Oops, a game is already running, use </b><code>{}cleargames</code><b> to end all active games.</b>",
        "games_cleared": "<emoji document_id=6007942490076745785>🧹</emoji> <b>All active games have been ended and cleared.</b>",
        "turn": "<b>🕹 The game has started!\n👀 The first turn goes to {}</b>!",
        "next_player": "<b>😱 It's {}'s turn next</b>",
        "not_your_turn": "⚠ It's not your turn!",
        "not_player": "❌ You're not participating in the game",
        "cooldown": "⚠ Not so fast!",
        "winner": "<b>🎉 Winner: {}</b>\n\n<b>👤 <a href='tg://openmessage?user_id={}'>{}</a> chose: {}</b> \n<b>👤<a href='tg://openmessage?user_id={}'>{}</a> chose: {}</b>",
        "draw": "<b>🤝 It's a draw!</b>\n\n<b>👤 <a href='tg://openmessage?user_id={}'>{}</a> chose: {}</b>\n<b>👤 <a href='tg://openmessage?user_id={}'>{}</a> chose: {}</b>",
        "error_play_yourself": "⚠ You can't play against yourself",
        "rock": "🪨 Rock",
        "scissors": "✂️ Scissors",
        "paper": "📄 Paper",
        "random": "🎲 Random choice",
    }
    
    strings_ru = {
        "searching": "<b>✌️ Игра «Камень, ножницы, бумага»</b>",
        "join_game": "👾 Присоединиться к игре",
        "game_started": "⚠ Игра уже началась",
        "game_already_running": "<emoji document_id=5255772095958229697>🤚</emoji> <b>Игра уже запущена, используйте </b><code>{}cleargames</code><b>, чтобы завершить все начатые игры.</b>",
        "games_cleared": "<emoji document_id=6007942490076745785>🧹</emoji> <b>Все активные игры были завершены и очищены.</b>",
        "turn": "<b>🕹 Игра началась!\n👀 Первый ход за {}</b>!",
        "next_player": "<b>😱 Следующий ходит {}</b>",
        "not_your_turn": "⚠ Это не ваш ход!",
        "not_player": "❌ Вы не участвуете в игре",
        "cooldown": "⚠ Не так быстро!",
        "winner": "<b>🎉 Победитель: {}</b>\n\n<b>👤 <a href='tg://openmessage?user_id={}'>{}</a> выбрал: {}</b> \n<b>👤<a href='tg://openmessage?user_id={}'>{}</a> выбрал: {}</b>",
        "draw": "<b>🤝 Ничья!</b>\n\n<b>👤 <a href='tg://openmessage?user_id={}'>{}</a> выбрал: {}</b>\n<b>👤 <a href='tg://openmessage?user_id={}'>{}</a> выбрал: {}</b>",
        "error_play_yourself": "⚠ Вы не можете играть с самим сабой",
        "rock": "🪨 Камень",
        "scissors": "✂️ Ножницы",
        "paper": "📄 Бумага",
        "random": "🎲 Случайный выбор",
    }

    def __init__(self):
        self.games = {}
        self.last_click_time = {}

    @loader.command(
        ru_doc="- Начать игру «Камень, ножницы, бумага»",
        alias="rps"
    )
    async def sgamerps(self, message):
        """- Start the game «Rock, Paper, Scissors»"""
        chat_id = message.chat_id
        player1_id = message.sender_id
        game_id = f"{chat_id}_{player1_id}"
        prefix = utils.escape_html(self.get_prefix())
        
        if game_id in self.games:
            await utils.answer(message, self.strings["game_already_running"].format(prefix))
            return

        self.games[game_id] = {
            "player1": player1_id,
            "player2": None,
            "choices": {},
            "current_turn": None,
        }

        await self.inline.form(
            message=message,
            text=self.strings["searching"],
            reply_markup=[
                [
                    {"text": self.strings['join_game'], "callback": self.join_game, "args": (game_id,),}
                ],
            ],
            disable_security=True,
        )
        
    async def join_game(self, call, game_id: str):
        game = self.games.get(game_id)
        player2_id = call.from_user.id
        
        current_time = time.time()
        if player2_id in self.last_click_time and current_time - self.last_click_time[player2_id] < 3:
            await call.answer(self.strings["cooldown"])
            return

        self.last_click_time[player2_id] = current_time

        if game["player1"] == player2_id:
            await call.answer(self.strings["error_play_yourself"])
            return

        if game["player2"] is not None:
            await call.answer(self.strings["game_started"])
            return

        game["player2"] = player2_id
        game["current_turn"] = random.choice([game["player1"], game["player2"]])

        await call.edit(
            text=self.strings["turn"].format(
                get_display_name(await self._client.get_entity(game["current_turn"]))
            ),
            reply_markup=[ 
                [
                    {"text": self.strings["rock"], "callback": self.make_choice, "args": (game_id, "rock")},
                    {"text": self.strings["scissors"], "callback": self.make_choice, "args": (game_id, "scissors")},
                    {"text": self.strings["paper"], "callback": self.make_choice, "args": (game_id, "paper")},
                ],
                [
                    {"text": self.strings["random"], "callback": self.make_choice, "args": (game_id, "random")},
                ],
            ]
        )

    async def make_choice(self, call, game_id: str, choice: str):
        game = self.games.get(game_id)
        current_time = time.time()
       
        if call.from_user.id in self.last_click_time and current_time - self.last_click_time[call.from_user.id] < 2:
            await call.answer(self.strings["cooldown"])
            return

        self.last_click_time[call.from_user.id] = current_time

        if call.from_user.id not in [game["player1"], game["player2"]]:
            await call.answer(self.strings["not_player"])
            return

        is_random = choice == "random"
        if is_random:
            choice = random.choice(["rock", "scissors", "paper"])

        game["choices"][call.from_user.id] = (choice, "random" if is_random else None)

        if len(game["choices"]) == 2:
            await self.resolve_game(call, game_id)
        else:
            game["current_turn"] = game["player1"] if call.from_user.id == game["player2"] else game["player2"]
            next_player = get_display_name(await self._client.get_entity(game['current_turn']))
            await call.edit(
                text=self.strings['next_player'].format(next_player),
                reply_markup=[ 
                    [
                        {"text": self.strings["rock"], "callback": self.make_choice, "args": (game_id, "rock")},
                        {"text": self.strings["scissors"], "callback": self.make_choice, "args": (game_id, "scissors")},
                        {"text": self.strings["paper"], "callback": self.make_choice, "args": (game_id, "paper")},
                    ],
                    [
                        {"text": self.strings["random"], "callback": self.make_choice, "args": (game_id, "random")},
                    ],
                ]
            )

    async def resolve_game(self, call, game_id: str):
        game = self.games.get(game_id)

        if not game:
            return

        player1_id = game["player1"]
        player2_id = game["player2"]

        player1_choice, player1_random = game["choices"].get(player1_id, (None, None))
        player2_choice, player2_random = game["choices"].get(player2_id, (None, None))

        if player1_choice is None or player2_choice is None:
            return

        player1_choice_text = self.strings[player1_choice]
        player2_choice_text = self.strings[player2_choice]

        if player1_random:
            player1_choice_text += " [🎲RANDOM]"
        if player2_random:
            player2_choice_text += " [🎲RANDOM]"

        if player1_choice == player2_choice:                
            result_message = self.strings["draw"].format(
                player1_id,
                utils.escape_html(get_display_name(await self._client.get_entity(player1_id))),
                player1_choice_text,
                player2_id,
                utils.escape_html(get_display_name(await self._client.get_entity(player2_id))),
                player2_choice_text,
            )
        else:
            winning_conditions = {
                "rock": "scissors",
                "scissors": "paper",
                "paper": "rock"
            }

            winner_id = player1_id if winning_conditions[player1_choice] == player2_choice else player2_id
            result_message = self.strings["winner"].format(
                utils.escape_html(get_display_name(await self._client.get_entity(winner_id))),
                winner_id,
                utils.escape_html(get_display_name(await self._client.get_entity(player1_id))),
                player1_choice_text,
                player2_id,
                utils.escape_html(get_display_name(await self._client.get_entity(player2_id))),
                player2_choice_text,
            )

        await call.edit(text=result_message)
        
        del self.games[game_id]
        
    async def call_del(self, call):
        await call.delete()
        
    @loader.command(
        ru_doc=f"- Завершить все активные игры.",
        alias="clg"
    )
    async def cleargames(self, message):
        """- Complete all running games."""
        self.games.clear()
        await utils.answer(message, self.strings["games_cleared"])
