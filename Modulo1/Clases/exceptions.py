num_1 = input("Ingresá el primer número: ")
num_2 = input("Ingresá el segundo número: ")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(f"El resultado de la división es {num_1 / num_2}")
except ValueError:
    print("No ingresaste dos valores numéricos.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
finally:
    print("El programa terminó.")
