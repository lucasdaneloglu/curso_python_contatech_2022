class Persona:
    def __init__(self, name: str, surname: str) -> None:
        self.__name = name
        self.__surname = surname

    def full_name(self) -> str:
        return self.__name + " " + self.__surname

    def initials(self) -> str:
        return self.__name[0] + "." + self.__surname[0] + "."
