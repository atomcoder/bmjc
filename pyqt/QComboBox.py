import sys
from PyQt5 import QtWidgets


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel('Ubuntu', self)
        combo = QtWidgets.QComboBox(self)
        combo.addItems(['Ubuntu', 'Mandriva', 'Fedora', 'Arch', 'Gentoo'])
        combo.activated[str].connect(self.onActivated)
        combo.move(50, 50)
        self.lbl.move(50, 150)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
