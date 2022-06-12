first_dice = input("Dame el valor del primer dado: ")
second_dice = input("Dame el valor del segundo dado: ")
third_dice = input("Dame el valor del tercer dado: ")
amount_of_six = [first_dice, second_dice, third_dice].count("6")

if amount_of_six == 1:
    print("Regular")
elif amount_of_six == 2:
    print("Muy bien!")
elif amount_of_six == 3:
    print("Excelente")
else:
    print("Insuficiente")
