import os
import re
import textract

def search_directory_for_word(directory, search_word):
    file_types = (".conf", ".txt", ".pdf", ".sh", ".docx", "", ".py")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_types):
                file_path = os.path.join(root, file)
                if file.endswith((".pdf", ".docx")):
                    try:
                        text = textract.process(file_path).decode("utf-8")
                    except (UnicodeDecodeError, textract.exceptions.ShellError):
                        # Do nothing if the file can't be read or if textract encounters an error
                        continue
                else:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            text = f.read()
                    except UnicodeDecodeError:
                        # Do nothing if the file can't be read
                        continue
                if re.search(search_word, text):
                    print(f"Word or phrase '{search_word}' found in file: {file_path}")

directory = input("Enter the directory: ")
search_word = input("Enter the word to search for: ")
search_directory_for_word(directory, search_word)
