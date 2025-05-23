import struct 

from .connection import Connection ,PacketCodec 

class AbridgedPacketCodec (PacketCodec ):
    tag =b'\xef'
    obfuscate_tag =b'\xef\xef\xef\xef'

    def encode_packet (self ,data ):
        length =len (data )>>2 
        if length <127 :
            length =struct .pack ('B',length )
        else :
            length =b'\x7f'+int .to_bytes (length ,3 ,'little')
        return length +data 

    async def read_packet (self ,reader ):
        length =struct .unpack ('<B',await reader .readexactly (1 ))[0 ]
        if length >=127 :
            length =struct .unpack (
            '<i',await reader .readexactly (3 )+b'\0')[0 ]

        return await reader .readexactly (length <<2 )

class ConnectionTcpAbridged (Connection ):
    """"""
    packet_codec =AbridgedPacketCodec 
