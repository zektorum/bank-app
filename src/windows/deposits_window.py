from PyQt5 import uic
from PyQt5.QtWidgets import QListWidgetItem

from src.user import User
from src.windows.main_menu_element import MainMenuElement


class DepositsWindow(MainMenuElement):
    def __init__(self, previous_window, user: User):
        super().__init__(previous_window)
        uic.loadUi("src/windows/ui/deposits.ui", self)

        self.user = user

        self.create_listview_items()
        self.exitPushButton.clicked.connect(self.exit_to_menu)

    def create_listview_items(self):
        for deposit in self.user.deposits:
            self.listWidget.addItem(QListWidgetItem(deposit.date + 70 * " " + deposit.type))
