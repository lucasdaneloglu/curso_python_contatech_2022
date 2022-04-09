PRODUCT_NAMES = ['esponja', 'bolsa de residuos', 'fósforos', 'detergente', 'servilletas', 'fin']
MESSAGE_TO_ASK_PRODUCT = f"Del siguiente listado: {PRODUCT_NAMES}\nIngresá el producto a comprar: "
MESSAGE_TO_ASK_QUANTITY = "Ingresá la cantidad: "
TAX_PRICE = 0.21
DISCOUNT_TEN_ITEMS = 0.03
tax_total_amount = 0
discount_total_amount = 0
sales_total_price = 0
sales_total = 0
inventory = {
    'esponja': {'stock': 150, 'amount': 70},
    'bolsa': {'stock': 70, 'amount': 120},
    'fosforos': {'stock': 50, 'amount': 85},
    'detergente': {'stock': 90, 'amount': 25},
    'servilletas': {'stock': 150, 'amount': 33},
}


def venta() -> None:
    final_price = 0
    product = get_valid_product()
    while product != 'fin':
        quantity = get_valid_quantity()
        final_price += calculate_final_price(product, quantity)
        update_stock(product, quantity)
        product = get_valid_product()
    print(f"El precio total de la venta es: ${final_price}")


def get_valid_product() -> str:
    product = ask_to_user(MESSAGE_TO_ASK_PRODUCT)
    is_product_valid = product in PRODUCT_NAMES
    while not is_product_valid:
        print("ERROR, el producto ingresado no es válido.")
        product = ask_to_user(MESSAGE_TO_ASK_PRODUCT)
        is_product_valid = product in PRODUCT_NAMES
    product.replace('ó', 'o').replace(' de residuos', '')
    return product


def ask_to_user(message) -> str:
    return input(message).lower()


def get_valid_quantity() -> int:
    user_input = input(MESSAGE_TO_ASK_QUANTITY)
    quantity = validate_quantity(user_input)
    return quantity


def validate_quantity(user_input: str) -> int:
    try:
        quantity = int(user_input)
        fail_if_negative_amount(quantity)
    except ValueError:
        print("ERROR, la cantidad ingresada no es válida.")
        quantity = get_valid_quantity()
    return quantity


def fail_if_negative_amount(quantity: int) -> None:
    if quantity < 0:
        raise ValueError


def update_stock(product: str, quantity: int) -> bool:
    if quantity <= inventory[product]['stock']:
        inventory[product]['stock'] -= quantity
    return quantity <= inventory[product]['stock']


def calculate_final_price(product: str, quantity: int) -> float:
    initial_price = inventory[product]['amount'] * quantity
    tax = initial_price * TAX_PRICE
    partial_price = initial_price + tax
    discount = 0
    if quantity >= 10:
        discount = partial_price - (partial_price * DISCOUNT_TEN_ITEMS)
    final_price = partial_price - discount
    update_global_args(tax, discount, final_price)
    return final_price


def update_global_args(tax: float, discount: float, final_price: float) -> None:
    global tax_total_amount, discount_total_amount, sales_total_price, sales_total
    tax_total_amount += tax
    discount_total_amount += discount
    sales_total_price += final_price
    sales_total += 1


def cierre_mensual() -> None:
    print(f"El impuesto total es: ${tax_total_amount}")
    print(f"El descuento total es: ${discount_total_amount}")
    print(f"El precio total de ventas es: ${sales_total_price}")
    for product in inventory:
        print(f"El stock de {product} es: {inventory[product]['stock']}")


venta()
cierre_mensual()
