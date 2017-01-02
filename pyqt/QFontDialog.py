import sys
from PyQt5 import QtWidgets


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox = QtWidgets.QVBoxLayout()
        btn = QtWidgets.QPushButton('Dialog', self)
        btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        btn.move(20, 20)
        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)
        self.lbl = QtWidgets.QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
    def showDialog(self):
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
