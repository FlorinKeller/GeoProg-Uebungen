import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
)

from PyQt6.uic import loadUi
from PyQt6.QtGui import QAction, QDesktopServices
from PyQt6.QtCore import QUrl, QDate


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("Übungen/showmap.ui", self)

        self.createConnects()
        self.show()

    def createConnects(self):
        self.button_karte.clicked.connect(self.showmap)

    def showmap(self):
        import urllib.parse

        coords = f"{self.lineEdit_laenge.text()},{self.lineEdit_breite.text()}"

        url = f"https://www.google.ch/maps/place/breite,länge/{urllib.parse.quote(coords)}"
        QDesktopServices.openUrl(QUrl(url))


def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()
    mainwindow.raise_()
    app.exec()


if __name__ == "__main__":
    main()
