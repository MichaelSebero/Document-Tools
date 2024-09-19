import os
import re
import textract
import magic
from collections import defaultdict

def search_directory_for_word(directory, search_word):
    text_extensions = ('.txt', '.conf', '.log', '.xml', '.json', '.yaml', '.yml', '.ini', '.cfg', '.properties', '.md', '.csv', '.tsv', '.html', '.htm', '.css', '.js', '.py', '.sh', '.bat', '.ps1', '.sql')
    special_types = ('.pdf', '.docx', '.doc', '.odt', '.rtf')
    results = defaultdict(lambda: defaultdict(list))
    total_matches = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = magic.from_file(file_path, mime=True)

            if file.lower().endswith(text_extensions) or file.lower().endswith(special_types) or file_type.startswith('text/'):
                try:
                    if file.lower().endswith(special_types):
                        text = textract.process(file_path).decode('utf-8')
                        lines = text.split('\n')
                    else:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                    
                    for i, line in enumerate(lines, 1):
                        if re.search(search_word, line, re.IGNORECASE):
                            results[root][file].append((i, line.strip()))
                            total_matches += 1
                
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")
                    continue

    return results, total_matches

def display_results(results, total_matches, search_word):
    if not results:
        print("No matches found.")
        return

    print(f"Total matches found: {total_matches}")
    print("=" * 80)

    for directory, files in results.items():
        print(f"\nDirectory: {directory}")
        print("-" * 80)
        for file, matches in files.items():
            print(f"  File: {file}")
            for line_num, line_content in matches:
                print(f"    Line {line_num}: {line_content}")
                highlighted_line = re.sub(f'({re.escape(search_word)})', r'\033[91m\1\033[0m', line_content, flags=re.IGNORECASE)
                print(f"      Matched: {highlighted_line}")
            print("-" * 40)
        print("=" * 80)

directory = input("Enter the directory to search: ")
search_word = input("Enter the word to search for: ")

results, total_matches = search_directory_for_word(directory, search_word)
display_results(results, total_matches, search_word)
