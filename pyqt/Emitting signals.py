import sys
from PyQt5 import QtWidgets, QtCore


class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()
class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
    def mousePressEvent(self, *args, **kwargs):
        self.c.closeApp.emit()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
