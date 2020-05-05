from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from updatedEx import MainMenu
import sys
import subprocess
import time #Only for testing closing and reopening the window
from CaptureData import Ui_CaptureData

class MyMenu(QtWidgets.QDialog):
    def __init__(self):
        super(MyMenu, self).__init__()
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
        time.sleep(1)
        # self.objectname=Kamy'sDialog()
        # test = self.objectname.exec_()
        # exec_ is a blocking action.
        #connect the Capture Data interface with the main menu
        
        self.CaptureDataForm=QtWidgets.QDialog()
        self.ui=Ui_CaptureData()
        self.ui.setupUi(CaptureDataForm)
        self.hide()
        self.CaptureData.show()
        
        #open a file from an existing directory
        self.ui.LoadDir_3.clicked.connect(self.file_open3)
        #self.ui.Deselect.clicked.connect(self.deselect_2)
        self.ui.Mainmenu.clicked.connect(self.backtomenu)
        #opening by a typed directory 
        # self.ui.commandLinkButton.clicked.connect(self.?)
        # self.objectname=Kamy'sDialog()
        # test = self.objectname.exec_()
        # exec_ is a blocking action. 
        
        # Re-open UI
     #  self.open()
     # Capture Data From an existing directory - Requires opening a file/folder?
   
        
        
    
    def file_open3(self):
        dirName = QFileDialog.getExistingDirectory()
        

       #def deselect_2(self):
        # update deselect_2 for deselecting in capturedatawidget
       # self.ui.Reg.setText("Hi")
    

    def backtomenu(self):
        self.dialog.hide()
        self.show()
        
    def registration(self):
        # call manual reg
        self.ui.Reg.setText("Hi")

    def dir_open(self):
        dirName = QFileDialog.getExistingDirectory()
        self.ui.DirText.setText("Directory Selected: " + dirName)
        if (dirName != ""): # i.e. they exit without selecting a directory
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
        # if (fileName != ""): # i.e. they exit without selecting a file
            # do something with file

    # View Mesh - Requires opening a file
    def file_open2(self):
        fileName = QFileDialog.getOpenFileName()
        # if (fileName != ""): # i.e. they exit without selecting a file
            # do something with file

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Menu = MyMenu()
    sys.exit(app.exec_())
