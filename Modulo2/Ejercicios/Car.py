# noinspection PyShadowingBuiltins
class Car:
    def __init__(self, brand: str, model: str, id: str, total_fuel: float, km_per_litre: float):
        self.brand = brand
        self.model = model
        self.id = id
        self.total_fuel = total_fuel
        self.current_fuel = total_fuel
        self.km_per_litre = km_per_litre

    def travel(self, km: float) -> bool:
        consumption = km * self.km_per_litre
        if consumption <= self.current_fuel:
            self.current_fuel -= consumption
            return True
        return False

    def refuel(self, recharge: float) -> bool:
        if self.__check_current_fuel(recharge):
            self.current_fuel += recharge
            return True
        return False

    def __check_current_fuel(self, recharge: float) -> bool:
        return recharge + self.current_fuel <= self.total_fuel
