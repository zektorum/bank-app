from PyQt5.QtWidgets import QMainWindow


class MainMenuElement(QMainWindow):
    def __init__(self, main_menu):
        super().__init__()
        self.main_menu = main_menu

    def exit_to_menu(self):
        self.main_menu.show()
        self.hide()
