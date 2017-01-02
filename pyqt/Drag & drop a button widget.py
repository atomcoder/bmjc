import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class Button(QtWidgets.QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return
        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.exec_(QtCore.Qt.MoveAction)

    def mousePressEvent(self, e):
        QtWidgets.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
            print('press')


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.button = Button('Button', self)
        self.button.move(100, 65)
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)
        self.show()

    def dragEnterEvent(self, QDragEnterEvent):
         QDragEnterEvent.accept()
         pass

    def dropEvent(self, QDropEvent):
        position = QDropEvent.pos()
        self.button.move(position)
        QDropEvent.setDropAction(QtCore.Qt.MoveAction)
        QDropEvent.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    # ex.show()
    # app.exec_()
    sys.exit(app.exec_())

