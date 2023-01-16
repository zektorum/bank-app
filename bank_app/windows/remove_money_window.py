from PyQt5 import uic

from bank_app.user import User
from bank_app.utils.money import remove_money
from bank_app.utils.window import create_dialog
from bank_app.utils.users import update_user
from bank_app.windows.main_menu_element import MainMenuElement


class RemoveMoneyWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("bank_app/windows/ui/remove_money.ui", self)

        self.user = user
        self.previous_window = previous_window

        self.enterPushButton.clicked.connect(self.remove_money)
        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def remove_money(self):
        currency = self.currencyComboBox.currentText()
        amount = float(self.amountLineEdit.text())
        remove_money(self.user, currency, amount)
        update_user(self.user)
        create_dialog(self, "Снятие", "Операция прошла успешно!")
