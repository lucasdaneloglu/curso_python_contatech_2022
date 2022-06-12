VALUE_HOUR_FULL_WORKDAY = 16
VALUE_HOUR_OVERTIME = 20
FULL_WORKDAY_HOURS = 40
hours_worked = int(input("Enter the number of hours worked: "))
overtime = hours_worked - FULL_WORKDAY_HOURS
salary = ((hours_worked - overtime) * VALUE_HOUR_FULL_WORKDAY)
salary_overtime = overtime * VALUE_HOUR_OVERTIME
total_salary = salary + salary_overtime
print("Salary: ", salary)
