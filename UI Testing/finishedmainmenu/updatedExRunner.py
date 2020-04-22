from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from updatedEx import MainMenu
import sys
import subprocess
import time #Only for testing closing and reopening the window

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = MainMenu()
        self.ui.setupUi(self)
        self.show()

        # Define button actions to functions 
        self.ui.CaptureData.clicked.connect(self.capture)
        self.ui.Reg.clicked.connect(self.registration)
        self.ui.LoadDir.clicked.connect(self.dir_open)
        self.ui.Deselect.clicked.connect(self.deselect)
        self.ui.ViewPointCloud.clicked.connect(self.file_open1)
        self.ui.ViewMesh.clicked.connect(self.file_open2)

    def capture(self):
        # Hide window
        self.hide()

        # do something
        time.sleep(2)

        # Re-open UI
        self.open()

    def registration(self):
        # call manual reg
        self.ui.Reg.setText("Hi")

    def dir_open(self):
        dirName = QFileDialog.getExistingDirectory()
        self.ui.DirText.setText("Directory Selected: " + dirName)
        if (dirName != ""): 
            self.ui.Reg.setEnabled(True) # Reg should be allowed only when a directory is selected
            self.ui.Deselect.setEnabled(True) # Deselect should be allowed only when a directory is selected

    def deselect(self):
        dirName = ""
        self.ui.DirText.setText("Directory Selected: " + dirName)
        self.ui.Reg.setEnabled(False)
        self.ui.Deselect.setEnabled(False)

    # View Point Cloud - Requires opening a file
    def file_open1(self):
        fileName = QFileDialog.getOpenFileName()
        # do something with file

    # View Mesh - Requires opening a file
    def file_open2(self):
        fileName = QFileDialog.getOpenFileName()
        # do something with file

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = MyDialog()
    sys.exit(app.exec_())
