# File handling and exceptions
from pathlib import Path

file_path = Path("sample_output.txt")

try:
    with file_path.open("w", encoding="utf-8") as file:
        file.write("Python file handling example\n")
        file.write("Second line\n")

    with file_path.open("r", encoding="utf-8") as file:
        print(file.read())

except OSError as error:
    print("File operation failed:", error)
