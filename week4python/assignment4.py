

#  Create a program that reads a file and writes a modified version to a new file.
with open("example.txt", "r") as file:
    data = file.read()
    # print(data)

with open("example_modified.txt", "w") as file:
    file.write(data.upper())
    file.write("\nWord count: " + str(len(data.split())))

# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename to read: ")
try:
    with open(filename, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
