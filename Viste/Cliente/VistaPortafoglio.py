from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestioneClienti import  GestioneClienti
from Utils.Const.PathViste import PATH_VISTA_PORTAFOGLIO


class VistaPortafoglio(QDialog):
    def __init__(self):
        super(VistaPortafoglio, self).__init__()
        loadUi(PATH_VISTA_PORTAFOGLIO, self)
        self.gestione_clienti = GestioneClienti()
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_back)
        self.confirm_button.clicked.connect(self.go_versamento)
        self.saldo_label_to_edit.setText(self.gestione_clienti.visualizza_portafoglio() + " €")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_versamento(self):
        value = self.quantita_da_versare.value()
        if value == 0:
            mb = QMessageBox()
            mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            mb.setWindowTitle("Attenzione")
            mb.setIcon(QMessageBox.Information)
            mb.setStyleSheet("background-color: rgb(255,255,255); color:rgb(0,0,0);")
            mb.setText("Inserire un valore maggiore di 0!")
            mb.exec()
        else:
            saldo = self.gestione_clienti.versa_denaro(value)
            self.saldo_label_to_edit.setText(saldo + " €")
            mb = QMessageBox()
            mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            mb.setWindowTitle("Attenzione")
            mb.setIcon(QMessageBox.Information)
            mb.setStyleSheet("background-color: rgb(255,255,255); color:rgb(0,0,0);")
            mb.setText("Denaro versato con successo!")
            mb.exec()

    def go_back(self):
        self.close()
