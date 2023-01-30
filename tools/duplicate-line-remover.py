import os

def sort_and_save_unique_lines(input_location):
    with open(input_location, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    unique_lines = sorted(set(lines))  # Fixed the missing parenthesis here

    # Extract the input file name without the path
    input_file_name = os.path.basename(input_location)

    # Construct the output file path in the same directory as the input file
    output_file_path = os.path.join(os.path.dirname(input_location), f"output_{input_file_name}")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(unique_lines)

    print(f"Sorting completed. Unique lines saved in {output_file_path}")

if __name__ == "__main__":
    # Get input file path from the user
    location_of_file = input("Enter the file path: ")

    # Sort and save unique lines to the output file in the same directory as the input file
    sort_and_save_unique_lines(location_of_file)
