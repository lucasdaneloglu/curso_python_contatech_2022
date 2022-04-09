class CreditCard:
    def __init__(self, number: str, customer: str, buy_limit: float, available_limit: float):
        self.__number = number
        self.__customer = customer
        self.__buy_limit = buy_limit
        self.__available_limit = available_limit

    def __can_buy(self, amount: float) -> bool:
        return amount <= self.__available_limit

    def buy(self, amount: float) -> bool:
        if self.__can_buy(amount):
            self.__available_limit -= amount
            return True
        return False

    def update_limit(self, new_limit: float) -> None:
        self.__available_limit = new_limit
