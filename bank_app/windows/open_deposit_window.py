from PyQt5 import uic

from bank_app.deposit import Deposit
from bank_app.user import User
from bank_app.utils.window import create_dialog
from bank_app.utils.users import update_user
from bank_app.windows.main_menu_element import MainMenuElement


class OpenDepositWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("bank_app/windows/ui/open_deposit.ui", self)

        self.user = user
        self.previous_window = previous_window

        self.enterPushButton.clicked.connect(self.open_deposit)
        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def open_deposit(self):
        date_obj = self.dateEdit.date()
        day, month, year = date_obj.day(), date_obj.month(), date_obj.year()
        date = f"{day}.{month}.{year}"
        amount = float(self.amountLineEdit.text())
        type = self.typeComboBox.currentText()
        self.user.deposits.append(Deposit(type, amount, date))
        update_user(self.user)
        create_dialog(self, "Открытие вклада", "Вклад успешно открыт!")
