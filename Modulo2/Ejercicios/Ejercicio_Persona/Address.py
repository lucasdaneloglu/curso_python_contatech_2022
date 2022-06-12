class Address:
    def __init__(self, street: str, number: str, city: str):
        self.__street = street
        self.__number = number
        self.__city = city

    def street(self, value: str) -> None:
        self.__street = value

    def number(self, value: str) -> None:
        self.__number = value

    def city(self, value: str) -> None:
        self.__city = value

    def __str__(self):
        return f"{self.__street}, {self.__number}, {self.__city}"
