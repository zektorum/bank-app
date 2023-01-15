from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/windows/ui/auth.ui", self)

        self.exitButton.clicked.connect(self.close)
