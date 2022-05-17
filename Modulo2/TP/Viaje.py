from Modulo2.TP.Botella import Botella


class Viaje:
    def __init__(self, tipo: str, fecha: str, botellas: list[Botella]):
        # TODO validar tipo igual que se validó variedad en Botella
        self.__tipo = tipo
        self.__fecha = fecha
        self.__botellas = botellas

    def calcular_precio_total(self) -> float:
        precio_total = 0
        for botella in self.__botellas:
            precio_total += botella.precio
        return precio_total
