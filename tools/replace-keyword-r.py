import os
import json

def replace_keyword_in_file(file_path, old_keyword, new_keyword):
    with open(file_path, 'r') as file:
        content = file.read()
        updated_content = content.replace(old_keyword, new_keyword)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)

def main():
    # Get user input
    directory_path = input("Enter the file path: ")
    old_keyword = input("Enter the keyword to replace: ")
    new_keyword = input("Enter the replacement keyword: ")

    # Iterate over files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if it's a file (not a directory) and has an extension
        if os.path.isfile(file_path) and '.' in filename:
            file_extension = filename.split('.')[-1]

            # Replace keyword only for supported file extensions (json, conf, txt)
            if file_extension.lower() in ('json', 'conf', 'txt'):
                replace_keyword_in_file(file_path, old_keyword, new_keyword)
                print(f"Replaced '{old_keyword}' with '{new_keyword}' in {filename}")

    print("Replacement process completed.")

if __name__ == "__main__":
    main()
