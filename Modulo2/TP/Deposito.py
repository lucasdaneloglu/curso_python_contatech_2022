from datetime import date

from Modulo2.TP.Botella import Botella
from Modulo2.TP.Viaje import Viaje


class Deposito:

    def __init__(self, stock: list[Botella]):
        self.__viajes = []
        self.__stock = stock
        self.__ingresos = 0
        self.__egresos = 0

    def ingreso(self, botellas: list[Botella]) -> None:
        self.__stock.extend(botellas)
        self.__viajes.append(Viaje('ingreso', date.today(), botellas))
        self.__ingresos += 1

    def egreso(self, botellas: list[Botella]) -> None:
        for botella in botellas:
            self.__stock.remove(botella)
        self.__viajes.append(Viaje('egreso', date.today(), botellas))
        self.__egresos += 1

    def cierre_mensual(self) -> None:
        self.__mostrar_stock()
        self.__mostrar_viajes()
        self.__mostrar_balance()

    def __mostrar_viajes(self) -> None:
        print('Viajes:')
        print(self.__ingresos)
        print(self.__egresos)
        print(f'Balance = {self.__ingresos - self.__egresos}')

    def __mostrar_stock(self) -> None:
        print('Stock:')
        for botella in self.__stock:
            print(botella)

    def __mostrar_balance(self) -> None:
        print(self.__calcular_balance_viajes())

    def __calcular_balance_viajes(self) -> float:
        balance = 0
        for viaje in self.__viajes:
            if viaje.tipo == 'ingreso':
                balance += viaje.calcular_precio_total()
            else:
                balance -= viaje.calcular_precio_total()
        return balance
