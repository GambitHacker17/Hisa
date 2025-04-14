import os
import re
REPLACEMENTS = {
    "Hisa": "Hisa",
    "hisa": "hisa"
}
TARGET_DIR = "."
SCRIPT_NAME = os.path.basename(__file__)
FILE_EXTENSIONS = {}
def replace_text_in_file(file_path):
    if os.path.basename(file_path) == SCRIPT_NAME:
        return  
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content
        for old, new in REPLACEMENTS.items():
            new_content = re.sub(rf"\b{old}\b", new, new_content)
        if new_content != content:  
            backup_path = file_path + ".bak"
            os.rename(file_path, backup_path)  
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Заменено в файле: {file_path}")
    except Exception as e:
        print(f"Ошибка обработки {file_path}: {e}")
def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file != SCRIPT_NAME and (not FILE_EXTENSIONS or any(file.endswith(ext) for ext in FILE_EXTENSIONS)):
                replace_text_in_file(os.path.join(root, file))
if __name__ == "__main__":
    process_directory(TARGET_DIR)
    print("Замена завершена.")