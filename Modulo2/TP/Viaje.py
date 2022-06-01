import datetime

from Modulo2.TP.Botella import Botella
from Modulo2.TP.TipoViajeInvalido import TipoViajeInvalido


class Viaje:
    tipos = ['ingreso', 'egreso']

    def __init__(self, tipo: str, fecha: datetime, botellas: list[Botella]):
        self.__tipo = tipo
        self.__fecha = fecha
        self.__botellas = botellas

    def __set_tipo(self, tipo: str) -> None:
        if not self.__es_tipo_valido(tipo):
            raise TipoViajeInvalido(f"El tipo {tipo} no es válido.")
        self.__tipo = tipo

    def __es_tipo_valido(self, tipo: str) -> bool:
        return tipo in Viaje.tipos

    def calcular_precio_total(self) -> float:
        precio_total = 0
        for botella in self.__botellas:
            precio_total += botella.precio
        return precio_total
