from PyQt5 import uic

from bank_app.user import User
from bank_app.windows.main_menu_element import MainMenuElement


class BalanceWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("bank_app/windows/ui/deposits_info.ui", self)

        self.user = user
        self.previous_window = previous_window
        self.label.setText(self.label.text().replace("XXXXXXXX", str(user.id)))

        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def update_balance(self):
        self.rubValueLabel.setText(str(self.user.balance.rub))
        self.usdValueLabel.setText(str(self.user.balance.usd))
        self.eurValueLabel.setText(str(self.user.balance.eur))