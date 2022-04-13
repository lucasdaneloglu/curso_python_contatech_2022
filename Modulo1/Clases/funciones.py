def saludar(name: str) -> None:
    print("Hola " + name + "!")


def es_par(number: int) -> bool:
    return number % 2 == 0


saludar('Juan')
saludar(str(1))

print("El cuatro es par: " + str(es_par(4)))
print("El seis es par: " + str(es_par(6)))
print("El tres es par: " + str(es_par(3)))
