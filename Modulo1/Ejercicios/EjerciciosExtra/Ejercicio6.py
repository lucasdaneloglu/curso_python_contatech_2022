total_capital = float(input("Enter total capital: "))
first_name = input("Enter name of first person: ")
first_contribution = float(input("Enter contribution of first person: "))
second_name = input("Enter name of second person: ")
second_contribution = float(input("Enter contribution of second person: "))
third_name = input("Enter name of third person: ")
third_contribution = float(input("Enter contribution of third person: "))
names = [first_name, second_name, third_name]
contributions = [first_contribution, second_contribution, third_contribution]
for i in range(len(names)):
    percentage_contribution = contributions[i] / total_capital * 100
    print(f'{names[i]} contributed %{percentage_contribution}')
print("Total capital:", total_capital)
