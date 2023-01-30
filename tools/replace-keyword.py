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
    file_path = input("Enter the file path: ")
    old_keyword = input("Enter the keyword to replace: ")
    new_keyword = input("Enter the replacement keyword: ")

    # Replace keyword in the file
    replace_keyword_in_file(file_path, old_keyword, new_keyword)
    print(f"Replaced '{old_keyword}' with '{new_keyword}' in {os.path.basename(file_path)}")

    print("Replacement process completed.")

if __name__ == "__main__":
    main()
