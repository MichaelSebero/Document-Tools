import os

def filter_and_save(file_path, keyword):
    # Read the contents of the file in binary mode
    with open(file_path, 'rb') as file:
        lines = file.readlines()

    # Filter lines containing the keyword
    filtered_lines = [line for line in lines if keyword.encode('utf-8') in line]

    # Write the filtered lines to a new file in binary mode
    output_path = os.path.splitext(file_path)[0] + "_filtered.txt"
    with open(output_path, 'wb') as output_file:
        output_file.writelines(filtered_lines)

    print(f"Filtered content saved to: {output_path}")

if __name__ == "__main__":
    # Get user input for file path and keyword
    file_path = input("Enter the file path: ")
    keyword = input("Enter the keyword: ")

    # Validate file existence
    if not os.path.isfile(file_path):
        print("Error: The specified file does not exist.")
    else:
        filter_and_save(file_path, keyword)
