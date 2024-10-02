import os

def replace_in_file(file_path, old_text, new_text):
    try:
        # Read the content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Perform replacement
        if old_text in content:
            updated_content = content.replace(old_text, new_text)
            
            # Write changes back
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def process_directory(directory_path, old_text, new_text):
    modified_files = 0
    total_files = 0
    
    # Walk through all files in directory and subdirectories
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_files += 1
            if replace_in_file(file_path, old_text, new_text):
                modified_files += 1
                print(f"Modified: {file_path}")
    
    return modified_files, total_files

def main():
    directory = input("Directory path: ")
    old_text = input("Text to replace: ")
    new_text = input("Replace with: ")

    if not os.path.isdir(directory):
        print("Error: Invalid directory path")
        return

    modified, total = process_directory(directory, old_text, new_text)
    print(f"\nComplete! Modified {modified} out of {total} files")

if __name__ == "__main__":
    main()
