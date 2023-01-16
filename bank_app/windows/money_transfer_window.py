from PyQt5 import uic

from bank_app.user import User
from bank_app.utils.money import replenish_balance, remove_money
from bank_app.utils.window import create_dialog
from bank_app.utils.users import find_user_in_db_by_id
from bank_app.utils.users import update_user
from bank_app.windows.main_menu_element import MainMenuElement


class MoneyTransferWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("bank_app/windows/ui/money_transfer.ui", self)

        self.user = user
        self.previous_window = previous_window

        self.enterPushButton.clicked.connect(self.transfer)
        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def transfer(self):
        currency = self.currencyComboBox.currentText()
        amount = float(self.amountLineEdit.text())
        recipient = int(self.recipientLineEdit.text())

        status = remove_money(self.user, currency, amount)
        if status == -1:
            create_dialog(self, "Ошибка", "Недостаточно средств")
            return
        recepient_user = find_user_in_db_by_id(recipient)
        replenish_balance(recepient_user, currency, amount)
        create_dialog(self, "Транзакция прошла успешно", "Средства поступили на счёт")
