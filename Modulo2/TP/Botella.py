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
        if self.__es_valida_variedad(variedad):
            self.__variedad = variedad
        else:
            raise VariedadBotellaInvalida(f"La variedad {variedad} no es válida.")

    # getter
    def precio(self):
        return self.__precio
