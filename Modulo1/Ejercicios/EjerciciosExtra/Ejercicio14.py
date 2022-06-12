best_name = ""
best_average = 0
for i in range(10):
    name = input("Enter the name of the student: ")
    average = float(input("Enter the average of the student: "))
    if average > best_average:
        best_average = average
        best_name = name
print("The best student is: ", best_name)
print("The best average is: ", best_average)
