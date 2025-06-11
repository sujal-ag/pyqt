from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1400, 200, 300, 300)         # x pos, y pos, width, height
        self.setWindowTitle("Learning PyQt")
        self.initUI()
    
    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("My First Element")
        self.label.move(50, 50)
        
        self.b1 = QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("The button is pressed")
        self.update()
    
    def update(self):
        self.label.adjustSize()


def windows():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

windows()