from PyQt4 import QtGui, QtCore
import sys

class First(QtGui.QMainWindow, design1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.setupUi(self)
        self.PushButtonFirst.clicked.connect(self.on_PushButtonFirst_clicked)
        self.partnerDialog = Second(self)

    def on_PushButtonFirst_clicked(self):
        self.partnerDialog.lineEditSecond.setText(self.lineEditFirst.text())
        self.partnerDialog.show()

class Second(QtGui.QMainWindow, design2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)
        self.PushButtonSecond.clicked.connect(self.on_PushButtonSecond_clicked)
        self.partnerDialog = parent  #otherwise, recursion

    def on_PushButtonSecond_clicked(self):
        self.partnerDialog.lineEditFirst.setText(self.lineEditSecond.text())
        self.partnerDialog.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    