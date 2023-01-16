from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from bank_app.user import User
from bank_app.windows.add_money import AddMoneyWindow
from bank_app.windows.balance_window import BalanceWindow
from bank_app.windows.deposits_window import DepositsWindow
from bank_app.windows.open_deposit import OpenDepositWindow


class MainMenu(QMainWindow):
    def __init__(self, auth_window, user: User):
        super().__init__()
        uic.loadUi("bank_app/windows/ui/main_menu.ui", self)

        self.user = user
        self.auth_window = auth_window

        self.balance_window = None
        self.deposits_window = None
        self.add_money_window = None
        self.open_deposit_window = None

        self.exitPushButton.clicked.connect(self.exit_to_auth)
        self.addPushButton.clicked.connect(self.add_money)
        self.statusPushButton.clicked.connect(self.show_balance)
        self.listDepositsPushButton.clicked.connect(self.show_deposits)
        self.addDepositPushButton.clicked.connect(self.add_deposit)

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

    def add_deposit(self):
        self.hide()
        self.open_deposit_window = OpenDepositWindow(self, self.user)
        self.open_deposit_window.show()

    def exit_to_auth(self):
        self.auth_window.show()
        self.hide()

