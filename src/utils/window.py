from PyQt5.QtWidgets import QMessageBox


def create_dialog(parent, title: str, message: str):
    dialog = QMessageBox(parent)
    dialog.setWindowTitle(title)
    dialog.setText(message)
    dialog.show()
