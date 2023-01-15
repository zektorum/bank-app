from json import loads
from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from src.user import User
from src.utils.window import create_dialog


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/windows/ui/auth.ui", self)

        self.users = self.get_users()
        self.submitButton.clicked.connect(self.auth)
        self.exitButton.clicked.connect(self.close)

    def auth(self):
        user = self.get_user_by_pin(self.pinInputField.text())
        if user is None:
            create_dialog(self, "Ошибка!", "Введён неверный PIN.")

    def get_users(self):
        data = ""
        with open("users.json", "r") as db:
            data = "".join(db.readlines())
        users_data = loads(data)
        return [User(**element) for element in users_data]

    def get_user_by_pin(self, pin: str) -> Optional[User]:
        if not pin.isnumeric():
            return
        for user in self.users:
            if user.pin == int(pin):
                return user
