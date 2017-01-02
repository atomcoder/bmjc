import sys
from PyQt5 import QtWidgets


class Button(QtWidgets.QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QtWidgets.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)
        button = Button('Button', self)
        button.move(190, 65)
        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
