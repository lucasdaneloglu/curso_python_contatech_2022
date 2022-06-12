total_subscription_a = 0
total_subscription_b = 0
total_subscription_c = 0
calls_less_than_sixs_minutes = 0
total_calls = 0
total_calls_price = 0


def customer_code() -> str:
    input_code = input("Ingrese el código de cliente: ")
    if len(input_code) != 5 and input_code != '0':
        print("El código debe tener 5 dígitos")
        return customer_code()
    return input_code


def call_duration() -> int:
    SECONDS_IN_SIX_MINUTES = 360
    input_duration = int(input("Ingrese la duración de la llamada en segundos: "))
    if input_duration <= 0:
        print("La duración de la llamada debe ser mayor a 0")
        return call_duration()
    if input_duration < SECONDS_IN_SIX_MINUTES:
        global calls_less_than_sixs_minutes
        calls_less_than_sixs_minutes += 1
    return input_duration


def subscription_type() -> str:
    input_type = input("Ingrese el tipo de abono [A, B, C]: ")
    if input_type not in ["A", "B", "C"]:
        print("El tipo de abono debe ser A, B o C")
        return subscription_type()
    return input_type


def calculate_price_type_a(duration: int) -> float:
    PRICE_A = 2
    price = PRICE_A * duration
    global total_subscription_a
    total_subscription_a += price
    return price


def calculate_price_type_b(duration: int) -> float:
    PRICE_A, PRICE_B = 2, 1.5
    extra_minutes = max(duration - 5, 0)
    price = abs((duration - extra_minutes) * PRICE_A) + (PRICE_B * extra_minutes)
    global total_subscription_b
    total_subscription_b += price
    return price


def calculate_price_type_c(duration: int) -> float:
    PRICE_C = 1
    price = PRICE_C * duration
    if duration > 10:
        price = 10
    global total_subscription_c
    total_subscription_c += price
    return price


def calculate_price(duration: int, subscription_type: str) -> float:
    if subscription_type == "A":
        return calculate_price_type_a(duration)
    elif subscription_type == "B":
        return calculate_price_type_b(duration)
    else:
        return calculate_price_type_c(duration)


def report():
    print("Total de abonos A: ", total_subscription_a)
    print("Total de abonos B: ", total_subscription_b)
    print("Total de abonos C: ", total_subscription_c)
    print("La cantidad de llamadas menores a 6 minutos es: ", calls_less_than_sixs_minutes)
    print("El promedio de llamadas es: ", total_calls_price / total_calls)


def calls_info():
    current_customer_code = customer_code()
    while current_customer_code != '0':
        current_call_duration = call_duration()
        current_subscription_type = subscription_type()
        final_call_price = calculate_price(current_call_duration, current_subscription_type)
        global total_calls_price
        global total_calls
        total_calls_price += final_call_price
        total_calls += 1
        current_customer_code = customer_code()


def main() -> None:
    calls_info()
    report()


if __name__ == '__main__':
    main()
