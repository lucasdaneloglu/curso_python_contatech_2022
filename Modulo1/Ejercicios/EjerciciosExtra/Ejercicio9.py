def format_date(input_date: str) -> str:
    day, month, year = input_date.split('/')
    return f'{year}/{month}/{day}'


date = input("Introduce la fecha (dd/mm/aaaa): ")
name = input("Introduce tu nombre: ")
name_of_product = input("Introduce el nombre del producto: ")
quantity = input("Introduce la cantidad: ")
price = input("Introduce el precio: ")

try:
    total_price = float(quantity) * float(price)
    date_formatted = format_date(date)
    print(f'Fecha de compra: {date_formatted}')
    print(f'Nombre del comprador: {name}')
    print(f'Producto solicitado: {name_of_product}')
    print(f'Cantidad solicitada: {quantity}')
    print(f'Precio unitario: {price}')
    print(f'Precio total: {total_price}')
except ValueError:
    print("Error: alguno de los datos ingresados es inválido.")
