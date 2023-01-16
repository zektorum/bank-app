from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from src.user import User
from src.utils.users import get_users
from src.utils.window import create_dialog
from src.windows.main_menu import MainMenu


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/windows/ui/auth.ui", self)

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
