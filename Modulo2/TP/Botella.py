from Modulo2.TP.VariedadBotellaInvalida import VariedadBotellaInvalida


class Botella:
    variedades = ['Lima', 'Cola', 'Naranja', 'Manzana']

    def __init__(self, variedad: str, precio: float):
        self.__set_variedad(variedad)
        self.__precio = precio

    def __es_valida_variedad(self, variedad: str) -> bool:
        return variedad in Botella.variedades

    # setter
    def __set_variedad(self, variedad: str) -> None:
        if not self.__es_valida_variedad(variedad):
            raise VariedadBotellaInvalida(f"La variedad {variedad} no es válida.")
        self.__variedad = variedad

    # getter
    def precio(self):
        return self.__precio

    def __str__(self):
        return f'Botella({self.__variedad}, {self.__precio})'
