import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('1.jpg'))
        self.label.setGeometry(160, 40, 80, 170)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('1.jpg'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('2.jpg'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('3.jpg'))
        else:
            self.label.setPixmap(QtGui.QPixmap('4.jpg'))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
