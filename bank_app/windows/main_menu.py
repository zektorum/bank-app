from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from bank_app.user import User
from bank_app.windows.add_money import AddMoneyWindow
from bank_app.windows.balance_window import BalanceWindow
from bank_app.windows.deposits_window import DepositsWindow


class MainMenu(QMainWindow):
    def __init__(self, auth_window, user: User):
        super().__init__()
        uic.loadUi("bank_app/windows/ui/main_menu.ui", self)

        self.user = user
        self.auth_window = auth_window

        self.balance_window = None
        self.deposits_window = None
        self.add_money_window = None

        self.exitPushButton.clicked.connect(self.exit_to_auth)
        self.addPushButton.clicked.connect(self.add_money)
        self.statusPushButton.clicked.connect(self.show_balance)
        self.listDepositsPushButton.clicked.connect(self.show_deposits)

    def show_balance(self):
        self.hide()
        self.balance_window = BalanceWindow(self, self.user)
        self.balance_window.show()

    def show_deposits(self):
        self.hide()
        self.deposits_window = DepositsWindow(self, self.user)
        self.deposits_window.show()

    def add_money(self):
        self.hide()
        self.add_money_window = AddMoneyWindow(self, self.user)
        self.add_money_window.show()

    def exit_to_auth(self):
        self.auth_window.show()
        self.hide()

