from datetime import datetime
from typing import List

from bank_app.balance import Balance
from bank_app.deposit import Deposit


class User:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.pin = kwargs["pin"]
        self.balance = self.create_balance(**kwargs["balance"])
        self.deposits = self.create_deposits(kwargs["deposits"])

    def create_balance(self, **kwargs):
        return Balance(kwargs["rub"], kwargs["eur"], kwargs["usd"])

    def create_deposits(self, deposits: List[dict]):
        return [Deposit(element.get("type"), element.get("amount"), element.get("date")) for element in deposits]

    def open_deposit(self, type: str, date: datetime):
        """
        Открытие нового вклада
        """
        pass

    def add_money(self, amount: float):
        """
        Пополнение баланса
        """
        pass

    def exchange_currency(self, currency_from: str, currency_to: str, amount: float):
        """
        Обмен валют
        """
        pass

    def update(self):
        """
        Обновляет данные пользователя в базе данных
        """
        pass
