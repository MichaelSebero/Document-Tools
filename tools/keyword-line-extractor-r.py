import os

def filter_and_save(file_path, keyword, output_file):
    # Read the contents of the file in text mode
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter lines containing the keyword
    filtered_lines = [line for line in lines if keyword in line]

    # Write the filtered lines to the output file in text mode
    with open(output_file, 'a') as output:
        output.writelines(filtered_lines)

def process_directory(directory, keyword, output_file):
    # Traverse through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            filter_and_save(file_path, keyword, output_file)

if __name__ == "__main__":
    # Get user input for directory and keyword
    directory = input("Enter the directory path: ")
    keyword = input("Enter the keyword: ")
    output_path = "output.txt"

    # Validate directory existence
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
    else:
        # Process the directory and save filtered content to output file
        process_directory(directory, keyword, output_path)

        print(f"Filtered content saved to: {output_path}")
