from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from src.user import User


class MainMenu(QMainWindow):
    def __init__(self, user: User):
        super().__init__()
        uic.loadUi("src/windows/ui/main_menu.ui", self)

        self.user = user
