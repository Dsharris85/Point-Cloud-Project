from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os.path
import sys
import threading
# imports for layout
from menulayout import MainMenu
from popup import Ui_CaptureData
from finishedcapture import *
# imports for functionality
from capture_test import *
from view import *
from run_system import *

# Class handling for main menu
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
        self.ui.ViewPointCloud.clicked.connect(self.view_pointcloud)
        self.ui.ViewMesh.clicked.connect(self.view_mesh)
        
    def capture(self):
        self.hide() # Hide window
        # Always pull up popup
        self.popup = CaptureDataDialog(self.dirName)
        test = self.popup.exec_() # Blocking action
        if (test): # If the user did not click the x in the corner
            self.dirName = self.popup.dirName
            self.ui.DirText.setText("Directory Selected: " + self.dirName)
            self.ui.Reg.setEnabled(True)
            self.ui.Deselect.setEnabled(True) 

            self.capturing = CaptureForm(self.dirName)
            test = self.capturing.exec_() # Blocking action
            
        self.show()
        
    def registration(self):
        self.hide()

        thread = threading.Thread(target=main_register_capture, args=[self.dirName])
        thread.start()
        thread.join()

        self.show()

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

    def view_pointcloud(self):
        fileName = QFileDialog.getOpenFileName()
        if (fileName != ""): # file must be selected
            self.hide()

            thread = threading.Thread(target=main_view_cloud, args=[fileName])
            thread.start()
            thread.join()

            self.show()

    def view_mesh(self):
        fileName = QFileDialog.getOpenFileName()
        if (fileName != ""): # file must be selected
            self.hide()

            thread = threading.Thread(target=main_view_mesh, args=[fileName])
            thread.start()
            thread.join()

            self.show()

# Class handling for popup dialog
class CaptureDataDialog(QtWidgets.QDialog):
    def __init__(self, givendirName):
        super(CaptureDataDialog, self).__init__()
        self.ui = Ui_CaptureData()
        self.ui.setupUi(self)
        self.show()
        # set up buttons
        self.ui.LoadDir_3.clicked.connect(self.dir_open)
        self.ui.Deselect.clicked.connect(self.deselect)
        self.ui.lineEdit.textChanged.connect(self.textchanged)
        self.ui.pushButton.clicked.connect(self.select)
        # set dirName from main menu, empty if nothing selected
        self.dirName = givendirName
        self.ui.lineEdit.setText(self.dirName)

    def dir_open(self):
        self.dirName = QFileDialog.getExistingDirectory()
        self.ui.lineEdit.setText(self.dirName)

    def deselect(self): # clears input
        self.dirName = ""
        self.ui.lineEdit.setText(self.dirName)
        self.ui.Deselect.setEnabled(False)
        
    def textchanged(self):
        if (self.ui.lineEdit.text() != ""):
            self.ui.Deselect.setEnabled(True) # enable deselect whenever text is input

    def select(self):
        self.dirName = self.ui.lineEdit.text()

        if not(os.path.isdir(self.dirName)): # warning for not a directory
            self.ui.DirText.setText("You did not enter in a valid directory.")
        else:
            self.accept() #exit out

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Menu = MyMenu()
    sys.exit(app.exec_())
