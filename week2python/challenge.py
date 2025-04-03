# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

# def create_list():
#     list = []

#     while True:
#         try:
#           numbers = int(input("Enter your numbers (or type 'done' to finish):"))
#           list.append(numbers)
#         except ValueError:
#            confirm = input("Do you want to exit (yes/no):")
#            if confirm == "yes":
#               break
           
#     return list

# def compute_sum(list):
#     return sum(list)

# user_numbers = create_list()
# total = compute_sum(user_numbers)

# print(f"\nYour List: {user_numbers}")
# print(f"\nSum of integers: {total} ")

user_input = input("Enter numbers separated by space:")

numbers = [int(num) for num in user_input.split()]

print("\nYour list:\n", numbers)
print("Sum of the integers: ", sum(numbers))


# 2. Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

myBooks = ("Pride and prejudice", "The Alchemist", "Things fall Apart", "Grain of wheat", "Who moved my cheese")

for book in myBooks:    
   print(book)

# 3. Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

person = {}

person["Name"] = input("Enter your name:")
person["Age"] = int(input("Enter your age:"))
person["Favorite_color"] = input("Enter your favorite color:")

print("\nYour details: \n")
print(person)

# 4. Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

user_input_1 = input("Enter numbers separated by space: ")
user_input_2 = input("Enter numbers separated by space: ")

set_1 = {int(num) for num in user_input_1.split()}
set_2 = {int(num) for num in user_input_2.split()}

print("\nYour first set:", set_1)
print("\nYour second set:", set_2)

print("Common set: ", set_1&set_2)

# 5. Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = ["apple", "orange", "mango", "banana", "lemon", "berry", "cherry"]

odd_number_words = [word for word in words if len(word) % 2 != 0]

print("\nOdd words: ", odd_number_words)