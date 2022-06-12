import sys


def calculate_seconds(hours_input: str, minutes_input: str, seconds_input: str) -> int:
    return int(hours_input) * SECONDS_PER_HOUR + int(minutes_input) * SECONDS_PER_MINUTE + int(seconds_input)


winner_number = 0
winner_seconds = sys.maxsize
total_seconds = 0
total_runners = 0
total_runners_fast = 0
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
number = input("Ingrese el número del corredor: ")
while int(number) != 0:
    total_runners += 1
    hours = input("Ingrese las horas: ")
    minutes = input("Ingrese los minutos: ")
    seconds = input("Ingrese los segundos: ")
    total_seconds = calculate_seconds(hours, minutes, seconds)
    total_runners_fast += 1 if total_seconds < SECONDS_PER_HOUR else 0
    if winner_seconds > total_seconds:
        winner_seconds = total_seconds
        winner_number = number
    number = input("Ingrese el número del corredor: ")

print("El ganador es el corredor número", winner_number, "con un tiempo de", winner_seconds, "segundos")
print("El promedio de segundos de carrera es de", total_seconds / total_runners, "segundos")
print("El total de corredores que terminaron en menos de una hora es de", total_runners_fast)
