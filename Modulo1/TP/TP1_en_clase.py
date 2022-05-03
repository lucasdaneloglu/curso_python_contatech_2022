gaseosas = {
    'lima': {'precio': 78, 'stock': 50},
    'cola': {'precio': 90, 'stock': 70},
    'naranja': {'precio': 52, 'stock': 50},
    'manzana': {'precio': 44, 'stock': 90}
}
ingresos_totales = 0
egresos_totales = 0


def procesar_ingreso() -> None:
    nombre = ''
    while nombre != "fin":
        print('-------------INGRESO-------------')
        nombre = input("Ingresá el nombre de la gaseosa: ")
        if nombre != "fin":
            try:
                cantidad = int(input("Ingresá la cantidad: "))
                incrementar_stock(cantidad, nombre)
            except ValueError:
                print("No ingresaste una cantidad válida, se esperaba un entero.")


def incrementar_stock(cantidad: int, nombre: str) -> None:
    try:
        gaseosas[nombre]['stock'] = gaseosas[nombre]['stock'] + cantidad
        global ingresos_totales
        ingresos_totales += 1
    except KeyError:
        print("La gaseosa ingresada no existe, por favor intentá de nuevo.")


def procesar_egreso() -> None:
    # TODO refactor
    nombre = ''
    while nombre != "fin":
        print('-------------EGRESO-------------')
        nombre = input("Ingresá el nombre de la gaseosa: ")
        if nombre != "fin":
            try:
                cantidad = int(input("Ingresá la cantidad: "))
                decrementar_stock(cantidad, nombre)
            except ValueError:
                print("No ingresaste una cantidad válida, se esperaba un entero.")


def decrementar_stock(cantidad: int, nombre: str) -> None:
    try:
        if gaseosas[nombre]['stock'] < cantidad:
            print(f"No hay stock suficiente de {nombre}, solo hay {gaseosas[nombre]['stock']}")
        else:
            gaseosas[nombre]['stock'] = gaseosas[nombre]['stock'] - cantidad
            global egresos_totales
            egresos_totales += 1
    except KeyError:
        print("La gaseosa ingresada no existe, por favor intentá de nuevo.")


def procesar_cierre_mensual() -> None:
    mostrar_stock_final()
    mostrar_balance_viajes()
    mostrar_balance_dinero()


def mostrar_balance_dinero() -> None:
    for gaseosa in gaseosas:
        valuacion_de_inventario = gaseosas[gaseosa]['stock'] * gaseosas[gaseosa]['precio']
        print(f"La valuación de inventario para {gaseosa} es: ${valuacion_de_inventario}")


def mostrar_balance_viajes() -> None:
    print(f"La cantidad de egresos totales es: {egresos_totales}")
    print(f"La cantidad de ingresos totales es: {ingresos_totales}")
    print(f"El balance total de viajes es: {egresos_totales - ingresos_totales}")


def mostrar_stock_final() -> None:
    for sabor in gaseosas:
        print(f"El stock para {sabor} es: {gaseosas[sabor]['stock']}")


def main() -> None:
    comando = ''
    while comando != "fin":
        comando = input("Ingresá la acción que querés realizar: [ingreso, egreso, cierre mensual] ")
        if comando == 'ingreso':
            procesar_ingreso()
        elif comando == 'egreso':
            procesar_egreso()
        elif comando == 'cierre mensual':
            procesar_cierre_mensual()
        else:
            print("El comando ingresado no es válido, los disponibles son [ingreso, egreso, cierre mensual]")
    print("FIN")


main()
