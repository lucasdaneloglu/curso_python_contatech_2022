from Modulo2.Clases.Calculadora import Calculadora


class Factura:
    iva = 1.21

    def __init__(self, numero: str, items: dict, codigo_cliente: str):
        self.numero = numero
        self.items = items
        self.codigo_cliente = codigo_cliente

    def __calcular_importe_item(self, codigo_item: int) -> float:
        try:
            item = self.items[codigo_item]
            return Calculadora.multiplicar(item["precio"], item["cantidad"])
        except KeyError:
            print(f'El item con codigo {codigo_item} no existe.')
            return -1

    @staticmethod
    def obtener_iva():
        return Factura.iva


factura = Factura("000-123-452", {
    1: {"codigo": "01", "cantidad": 12, "precio": 150},
    2: {"codigo": "02", "cantidad": 10, "precio": 15.50},
}, "0048")
print(f'El importe del item 1 es {factura.calcular_importe_item(1)}')
print(f'El importe del item 3 es {factura.calcular_importe_item(3)}')
print(Factura.obtener_iva())
