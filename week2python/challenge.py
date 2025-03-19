# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

def create_list():
    list = []

    while True:
        try:
          numbers = int(input("Enter your numbers (or type 'done' to finish):"))
          list.append(numbers)
        except ValueError:
           confirm = input("Do you want to exit (yes/no):")
           if confirm == "yes":
              break
           
    return list

def compute_sum(list):
    return sum(list)

user_numbers = create_list()
total = compute_sum(user_numbers)

print(f"\nYour List: {user_numbers}")
print(f"\nSum of integers: {total} ")


# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

myBooks = ("Pride and prejudice", "The Alchemist", "Things fall Apart", "Grain of wheat", "Who moved my cheese")

for book in myBooks:    
   print(book)