import sys


# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Get the filename from the command-line arguments
filename = sys.argv[1]

# Open the file for reading
try:
    with open(filename, 'r') as file:
        # Read and print the contents of the file
        for line in file:
            print(line.strip())  # strip() removes the newline character at the end of each line
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")