# listas
ages = [15, 26, 30, 33, 20]

# tupla
names = ('Bruno', 'Maria', 'Fernando', 'Juliana', 'Pedro')

ages[3] = 34
# names[3] = 'Mariana' NO PERMITIDO

index = 0
print(ages)
while index < len(ages):
    ages[index] = ages[index] + 1
    index += 1
    # index = index + 1
print('Salió del ciclo')
print(ages)

for name in names:
    print(name)

for number in range(0, 10, 2):
    print(number)
