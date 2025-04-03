


def calculate_discount(price, discount_percent):
    if  discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return (price - discount_amount)
    else:
        return price

price = float(input("Enter Price: "))
discount = float(input("Enter Discount: "))

# print(calculate_discount(2000,25))
print("Final Price: ", calculate_discount(price, discount))

        