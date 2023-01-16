from PyQt5 import uic

from bank_app.user import User
from bank_app.utils.window import create_dialog
from bank_app.utils.users import update_user
from bank_app.windows.main_menu_element import MainMenuElement


class AddMoneyWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("bank_app/windows/ui/add_money.ui", self)

        self.user = user
        self.previous_window = previous_window

        self.enterPushButton.clicked.connect(self.add_money)
        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def add_money(self):
        currency = self.currencyComboBox.currentText()
        amount = float(self.lineEdit.text())
        if currency == "RUB":
            self.user.balance.rub += amount
        if currency == "USD":
            self.user.balance.usd += amount
        if currency == "EUR":
            self.user.balance.eur += amount
        update_user(self.user)
        create_dialog(self, "Пополнение", "Операция прошла успешно!")
