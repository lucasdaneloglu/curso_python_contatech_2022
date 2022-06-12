number = input("Enter a number of the week: ")
numbers_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
try:
    number_as_integer = int(number)
    if number_as_integer in numbers_of_week:
        print(f"The day of the week is {numbers_of_week[number_as_integer]}")
    else:
        print("The number is not in the week")
except ValueError:
    print("The number is not in the week")
