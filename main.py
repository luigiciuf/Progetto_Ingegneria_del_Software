import sys

from PyQt5.QtWidgets import QApplication

from Viste.Accesso.Login import Login
import ctypes

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Login()
    mainwindow.show()
    sys.exit(app.exec())
