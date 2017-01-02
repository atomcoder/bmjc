import sys
from PyQt5 import QtWidgets, QtCore


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QtWidgets.QHBoxLayout(self)
        topleft = QtWidgets.QFrame(self)
        topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        topright = QtWidgets.QFrame(self)
        topright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        bottom = QtWidgets.QFrame(self)
        bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self, text):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
