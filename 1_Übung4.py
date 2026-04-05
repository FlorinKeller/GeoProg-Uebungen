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
)
from PyQt6.QtGui import QAction


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

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        filemenu.addAction(save)
        filemenu.addAction(quit)

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
        self.saveButton = QPushButton("Save")

        self.saveButton.clicked.connect(self.menu_save)

        ## Layout füllen
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.AdresseLineEdit)
        layout.addRow("Postleitzahl:", self.PostleitzahlLineEdit)
        layout.addRow("Ort:", self.OrtLineEdit)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.saveButton)

        ## Fenster anzeigen
        self.show()

    def createConnects(self):
        pass

    def menu_save(self):
        daten = f"{self.vornameLineEdit.text()},{self.nameLineEdit.text()},{self.geburtstagLineEdit.date().toString()},{self.AdresseLineEdit.text()},{self.PostleitzahlLineEdit.text()},{self.OrtLineEdit.text()},{self.Land.currentText()}\n"
        with open("output.txt", "a", encoding="utf-8") as file:
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
