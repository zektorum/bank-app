from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from bank_app.user import User
from bank_app.utils.users import get_users
from bank_app.utils.window import create_dialog
from bank_app.windows.main_menu_window import MainMenu


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("bank_app/windows/ui/auth.ui", self)

        self.users = get_users()
        self.submitButton.clicked.connect(self.auth)
        self.exitButton.clicked.connect(self.close)

        self.menu = None

    def auth(self):
        user = self.get_user_by_pin(self.pinInputField.text())
        if user is None:
            create_dialog(self, "Ошибка!", "Введён неверный PIN.")
        else:
            self.pinInputField.setText("")
            self.hide()
            self.menu = MainMenu(self, user)
            self.menu.show()

    def get_user_by_pin(self, pin: str) -> Optional[User]:
        if not pin.isnumeric():
            return
        for user in self.users:
            if user.pin == int(pin):
                return user
