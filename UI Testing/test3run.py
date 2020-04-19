from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from test3 import Ui_Dialog
import sys
import subprocess
import time #Only for testing closing and reopening the window

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton.clicked.connect(self.closewin)
        self.ui.pushButton_2.clicked.connect(self.file_open)
        self.ui.pushButton_3.clicked.connect(self.dir_open)
        self.ui.pushButton_4.clicked.connect(self.deselect)
        self.ui.pushButton_5.clicked.connect(self.auto)
        self.ui.pushButton_6.clicked.connect(self.manual)

    def closewin(self):
        # Hide window
        self.hide()

        # do something until child returns exit call
        time.sleep(2)

        # Re-open UI
        self.open()

    def file_open(self):
        fileName = QFileDialog.getOpenFileName()
        # do something with file

    def dir_open(self):
        dirName = QFileDialog.getExistingDirectory()
        self.ui.label.setText("Directory Selected: " + dirName)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)

    def deselect(self):
        dirName = " "
        self.ui.label.setText("Directory Selected: " + dirName)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)

    def manual(self):
        # call manual reg
        self.ui.pushButton_6.setText("Hi")

    def auto(self):
        # call auto reg
        self.ui.pushButton_5.setText("Hi")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = MyDialog()
    sys.exit(app.exec_())

