import sys
from PyQt5 import QtWidgets, QtGui


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QtWidgets.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('1.jpg')
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setPixmap(pixmap)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        self.move(300, 200)
        self.setWindowTitle('QPixmap')
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
