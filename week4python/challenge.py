


#  Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

with open("input.txt", "r") as file:
    data = file.read()
    # print(data)

word_count = len(data.split())

word_upper = data.upper()
    
with open("output.txt", "w") as file:
    file.write(word_upper)
    file.write("\nWord count: " + str(word_count))

print("\nFile successfully created.\n")