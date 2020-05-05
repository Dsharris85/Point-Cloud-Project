from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os.path
import sys
import subprocess
import time #Only for testing closing and reopening the window
from updatedEx import MainMenu
from CaptureDataEdited import Ui_CaptureData

class MyMenu(QtWidgets.QDialog):
    def __init__(self):
        super(MyMenu, self).__init__()
        self.ui = MainMenu()
        self.ui.setupUi(self)
        self.show()
        self.dirName = ""

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

        self.popup = CaptureDataDialog(self.dirName)
        test = self.popup.exec_()
        if (test):
            self.dirName = self.popup.dirName
            self.ui.DirText.setText("Directory Selected: " + self.dirName)
            self.ui.Reg.setEnabled(True)
            self.ui.Deselect.setEnabled(True) 

            #call main(dirName)

        self.open()
        
    def registration(self):
        # call manual reg
        self.ui.Reg.setText("Hi")

    def dir_open(self):
        self.dirName = QFileDialog.getExistingDirectory()
        self.ui.DirText.setText("Directory Selected: " + self.dirName)
        if (self.dirName != ""): # i.e. they exit without selecting a directory
            self.ui.Reg.setEnabled(True) # Reg should be allowed only when a directory is selected
            self.ui.Deselect.setEnabled(True) # Deselect should be allowed only when a directory is selected

    def deselect(self):
        self.dirName = ""
        self.ui.DirText.setText("Directory Selected: " + self.dirName)
        
        self.ui.Reg.setEnabled(False)
        self.ui.Deselect.setEnabled(False)

    # View Point Cloud - Requires opening a file
    def file_open1(self):
        fileName = QFileDialog.getOpenFileName()
        # if (fileName != ""): # i.e. they exit without selecting a file
            # do something with file

    # View Mesh - Requires opening a file
    def file_open2(self):
        fileName = QFileDialog.getOpenFileName()
        # if (fileName != ""): # i.e. they exit without selecting a file
            # do something with file

class CaptureDataDialog(QtWidgets.QDialog):
    def __init__(self, givendirName):
        super(CaptureDataDialog, self).__init__()
        self.ui = Ui_CaptureData()
        self.ui.setupUi(self)
        self.show()

        self.ui.LoadDir_3.clicked.connect(self.dir_open)
        self.ui.Deselect.clicked.connect(self.deselect)
        self.ui.lineEdit.textChanged.connect(self.textchanged)
        self.ui.pushButton.clicked.connect(self.select)

        self.dirName = givendirName
        self.ui.lineEdit.setText(self.dirName)

    def dir_open(self):
        self.dirName = QFileDialog.getExistingDirectory()
        self.ui.lineEdit.setText(self.dirName)

    def deselect(self):
        self.dirName = ""
        self.ui.lineEdit.setText(self.dirName)
        self.ui.Deselect.setEnabled(False)
        
    def textchanged(self):
        if (self.ui.lineEdit.text() != ""):
            self.ui.Deselect.setEnabled(True)

    def select(self):
        self.dirName = self.ui.lineEdit.text()

        if not(os.path.isdir(self.dirName)):
            self.ui.DirText.setText("You did not enter in a valid directory.")
        else:
            self.ui.DirText.setText("")
            self.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Menu = MyMenu()
    sys.exit(app.exec_())
