def is_odd(number) -> bool:
    return number % 2 != 0


input_number = input("Enter a number: ")
try:
    result = "The number is odd" if is_odd(int(input_number)) else "The number is even"
    print(result)
except ValueError:
    print("The number is not an integer")
