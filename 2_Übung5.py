from fileinput import filename
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QComboBox,
    QDateEdit,
    QFileDialog,
)
from PyQt6.QtGui import QAction, QDesktopServices
from PyQt6.QtCore import QUrl, QDate


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("GUI-Programmierung")

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        view = QAction("Karte anzeigen", self)
        view.triggered.connect(self.karte_anzeigen)

        laden = QAction("Laden", self)
        laden.triggered.connect(self.menu_laden)

        filemenu.addAction(save)
        filemenu.addAction(quit)
        viewmenu.addAction(view)
        filemenu.addAction(laden)

        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(800, 200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        ## Widgets erstellen

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.geburtstagLineEdit.setCalendarPopup(True)
        self.geburtstagLineEdit.setDate(QDateEdit().date().currentDate())
        self.AdresseLineEdit = QLineEdit()
        self.PostleitzahlLineEdit = QLineEdit()
        self.OrtLineEdit = QLineEdit()
        self.Land = QComboBox()
        self.Land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.mapButton = QPushButton("Auf Karte anzeigen")
        self.ladenButton = QPushButton("Laden")
        self.saveButton = QPushButton("Save")

        ## Layout füllen
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.AdresseLineEdit)
        layout.addRow("Postleitzahl:", self.PostleitzahlLineEdit)
        layout.addRow("Ort:", self.OrtLineEdit)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.mapButton)
        layout.addRow(self.ladenButton)
        layout.addRow(self.saveButton)

        ## Fenster anzeigen
        self.show()

    def createConnects(self):
        self.ladenButton.clicked.connect(self.menu_laden)
        self.mapButton.clicked.connect(self.karte_anzeigen)
        self.saveButton.clicked.connect(self.menu_save)

    # def karte_anzeigen(self):
    # import urllib.parse
    # import webbrowser

    # adresse = f"{self.AdresseLineEdit.text()} {self.PostleitzahlLineEdit.text()} {self.OrtLineEdit.text()} {self.Land.currentText()}"
    # url = f"https://www.google.com/maps/search/{urllib.parse.quote(adresse)}"
    # webbrowser.open(url)

    def karte_anzeigen(self):
        import urllib.parse

        adresse = f"{self.AdresseLineEdit.text()} {self.PostleitzahlLineEdit.text()} {self.OrtLineEdit.text()} {self.Land.currentText()}"
        url = f"https://www.google.com/maps/search/{urllib.parse.quote(adresse)}"
        QDesktopServices.openUrl(QUrl(url))

    def menu_laden(self):
        filename, typ = QFileDialog.getOpenFileName(
            self, "Datei öffnen", "", "Alle (*.*)"
        )
        if not filename:
            return
        with open(filename, "r", encoding="utf-8") as file:
            daten = file.read().strip().split(",")
        self.vornameLineEdit.setText(daten[0])
        self.nameLineEdit.setText(daten[1])
        self.geburtstagLineEdit.setDate(
            self.geburtstagLineEdit.date().fromString(daten[2])
        )
        self.AdresseLineEdit.setText(daten[3])
        self.PostleitzahlLineEdit.setText(daten[4])
        self.OrtLineEdit.setText(daten[5])
        self.Land.setCurrentText(daten[6])

    def menu_save(self):
        filename, typ = QFileDialog.getSaveFileName(
            self, "Datei speichern", "", "Alle (*.*)"
        )
        if not filename:
            return
        daten = f"{self.vornameLineEdit.text()},{self.nameLineEdit.text()},{self.geburtstagLineEdit.date().toString()},{self.AdresseLineEdit.text()},{self.PostleitzahlLineEdit.text()},{self.OrtLineEdit.text()},{self.Land.currentText()}\n"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(daten)
        self.close()

    def menu_quit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()
    mainwindow.raise_()
    app.exec()


if __name__ == "__main__":
    main()
