from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from src.user import User
from src.windows.balance_window import BalanceWindow
from src.windows.deposits_window import DepositsWindow


class MainMenu(QMainWindow):
    def __init__(self, user: User):
        super().__init__()
        uic.loadUi("src/windows/ui/main_menu.ui", self)

        self.user = user

        self.balance_window = None
        self.deposits_window = None

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

