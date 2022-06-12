first_number = int(input("Introduce the first number: "))
second_number = int(input("Introduce the second number: "))
result = 0
for i in range(0, second_number):
    result += first_number
print(f'El resultado es {result}')
