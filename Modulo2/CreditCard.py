class CreditCard:
    def __init__(self, number: str, customer: str, buy_limit: float, available_limit: float):
        self.number = number
        self.customer = customer
        self.buy_limit = buy_limit
        self.available_limit = available_limit

    def __can_buy(self, amount: float) -> bool:
        return amount <= self.available_limit

    def buy(self, amount: float) -> bool:
        if self.__can_buy(amount):
            self.available_limit -= amount
            return True
        return False

    def update_limit(self, new_limit: float) -> None:
        self.available_limit = new_limit