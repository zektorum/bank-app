import sys

from windows.auth_window import AuthWindow

from PyQt5.QtWidgets import QApplication


def excepthook(cls, traceback, exception):
    sys.excepthook(cls, traceback, exception)


def main():
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.excepthook = excepthook
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
