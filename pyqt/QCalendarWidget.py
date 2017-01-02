import sys
from PyQt5 import QtWidgets, QtCore


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QtWidgets.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        self.lbl = QtWidgets.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText('Calender')
        self.lbl.adjustSize()
        #self.lbl.resize(120, 20)
        self.lbl.move(130, 260)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
