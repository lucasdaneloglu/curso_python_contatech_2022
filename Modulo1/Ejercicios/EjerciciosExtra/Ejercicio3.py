operation = input("What do you want to do? (+, -, *, /): ")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("Invalid operation")

