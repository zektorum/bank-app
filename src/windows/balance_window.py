from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from src.user import User


class BalanceWindow(QMainWindow):
    def __init__(self, previous_window, user: User):
        super().__init__()
        uic.loadUi("src/windows/ui/deposits_info.ui", self)

        self.user = user
        self.previous_window = previous_window
        self.label.setText(self.label.text().replace("XXXXXXXX", str(user.id)))

        self.rubValueLabel.setText(str(user.balance.rub))
        self.usdValueLabel.setText(str(user.balance.usd))
        self.eurValueLabel.setText(str(user.balance.eur))

        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def exit_to_menu(self):
        self.previous_window.show()
        self.hide()
