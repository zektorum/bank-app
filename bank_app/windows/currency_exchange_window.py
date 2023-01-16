from PyQt5 import uic

from bank_app.user import User
from bank_app.utils.money import replenish_balance, remove_money, convert_currency
from bank_app.utils.window import create_dialog
from bank_app.utils.users import update_user
from bank_app.windows.main_menu_element import MainMenuElement


class CurrencyExchangeWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("bank_app/windows/ui/currency_exchange.ui", self)

        self.user = user
        self.previous_window = previous_window

        self.enterPushButton.clicked.connect(self.exchange)
        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def exchange(self):
        currency_from = self.currencyFromComboBox.currentText()
        currency_to = self.currencyToComboBox.currentText()
        if currency_from == currency_to:
            create_dialog(self, "Ошибка", "Выбраны две одинаковые валюты")
            return
        amount = float(self.amountLineEdit.text())
        result = convert_currency(currency_from, currency_to, amount)
        status = remove_money(self.user, currency_from, amount)
        if status == -1:
            create_dialog(self, "Ошибка", "Недостаточно средств")
            return
        replenish_balance(self.user, currency_to, result)
        update_user(self.user)
        create_dialog(self, "Обмен выполнен успешно",
                      f"Со счёта списано {amount} {currency_from} и зачислено {result} {currency_to}")
