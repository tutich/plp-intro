
# Activity 1
class Book:

    def __init__(self, category, author, title):
        self.category = category
        self.author = author
        self.title = title

        
    def display_info(self):
        print(f"'{self.title}' by {self.author} [{self.category}]")


class Library(Book):
    def __init__(self, category, author, title, shelf):
        super().__init__(category, author, title)
        self.shelf = shelf
        # self.category = category
        # self.author = author
        # self.title = title 
        # self.shelf = shelf

    def display_info(self): 
        print(f"'{self.title}' by {self.author} on Shelf {self.shelf}")


book1 = Book("Fiction", "George Orwell", "1984")
book2 = Library("Non-Fiction", "Malcolm Gladwell", "Outliers", "A5") 

book1.display_info()
book2.display_info()

# Activity 2
class Car:
    def move(self):
        print("The car is moving")

class Plane:
    def move(self):
        print("The plane is flying")

