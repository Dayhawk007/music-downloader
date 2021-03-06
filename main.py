from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QPushButton, QLabel
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QThread

import colors
import youtubedl


class Thread(QThread):
    def __init__(self, name):
        QThread.__init__(self)
        self.name = name

    # def setName(self,name):
    #  self.name = name
    def run(self):
        youtubedl.run(self.name)
        print(colors.green + "Downloaded!\n", colors.reset)


class homepage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    status_thread = False
    name = ""

    def initUI(self):
        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle("Music-downloader")
        self.setWindowIcon(QIcon('music.webp'))
        self.textbox = QLineEdit(self)
        self.label = QLabel("Song Name/Playlist link", self)
        self.btn = QPushButton('Download', self)
        self.label.move(20, 100)
        self.label.resize(150, 30)
        self.btn.move(270, 200)
        self.btn.resize(70, 30)
        self.textbox.move(150, 100)
        self.textbox.resize(400, 30)
        self.msg = QMessageBox(self)
        self.btn.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.setWindowTitle("Music-downloader(downloading)")
        name = self.textbox.text()
        self.thread = Thread(name)
        self.thread.start()


def main():
    app = QApplication(sys.argv)
    hp = homepage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
