
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

operation = input("Enter Operation (+, -, *, /):")

if operation == "+":
 result = num1 + num2
elif operation == "-":
 result = num1 - num2
elif operation == "*":
 result = num1 * num2
elif operation == "/":
 if num2 != 0: 
  result = num1/num2
 else:
  result = "Error"
else:
 result = "Invalid"

print("Answwer:", result)