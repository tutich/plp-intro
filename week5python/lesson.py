

# class Car:
#     color = "red"

#     def drive(self):
#         print("I can drive my car")

# car_color = Car()
# print(car_color.color)
# car_color.drive()


# class Car:

#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

# car1 = Car("blue", "sedan")
# car2 = Car("red", "SUV")

# print(car2.color)


class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())