# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QtWidgets.QToolTip.setFont(QtGui.QFont('仿宋', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('PyQt5_Demo1')
        self.setWindowIcon(QtGui.QIcon('1.jpg'))
        self.center()
        self.statusBar().showMessage('Ready')

        exitAction = QtWidgets.QAction(QtGui.QIcon('1.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtWidgets.qApp.quit)

        exitAction1 = QtWidgets.QAction(QtGui.QIcon('1.jpg'), '&Exit1', self)
        exitAction1.setShortcut('Ctrl+Q')
        exitAction1.setStatusTip('Exit application')
        exitAction1.triggered.connect(QtWidgets.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu1 = menubar.addMenu('&File1')
        fileMenu.addAction(exitAction)
        fileMenu1.addAction(exitAction1)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        btn = QtWidgets.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        quit_btn = QtWidgets.QPushButton('&Quit', self)
        quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(50, 50)

        textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(textEdit)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        replay = QtWidgets.QMessageBox.question(self, 'Message', 'Are U sure to quit?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if replay == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
