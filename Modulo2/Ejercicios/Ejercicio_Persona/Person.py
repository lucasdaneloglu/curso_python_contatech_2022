from Modulo2.Ejercicios.Ejercicio_Persona.Address import Address


class Person:
    def __init__(self):
        self.__address = None
        self.__name = ''
        self.__surname = ''

    def name(self, value: str) -> None:
        self.__name = value

    def surname(self, value: str) -> None:
        self.__surname = value

    def address(self, address: Address) -> None:
        self.__address = address

    def full_name(self):
        return f'{self.__name} {self.__surname}'

    def __str__(self):
        return f'{self.__name} {self.__surname}, vive en {self.__address}'
