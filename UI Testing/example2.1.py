
    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example2.1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from OtherWindow import Ui_MainWindow

class Ui_PointCloudProject(object):
    def setupUi(self, PointCloudProject):
        PointCloudProject.setObjectName("PointCloudProject")
        PointCloudProject.resize(356, 221)
        PointCloudProject.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        PointCloudProject.setFont(font)
        PointCloudProject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        PointCloudProject.setStyleSheet("background-color: rgb(231, 255, 253);\n"
"border-top-color: rgb(85, 0, 0);\n"
"border-right-color: rgb(85, 0, 0);\n"
"border-bottom-color: rgb(85, 0, 0);\n"
"border-left-color: rgb(85, 0, 0);")
        self.ViewPointCloud = QtWidgets.QPushButton(PointCloudProject)
        self.ViewPointCloud.setGeometry(QtCore.QRect(20, 110, 321, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewPointCloud.sizePolicy().hasHeightForWidth())
        self.ViewPointCloud.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.ViewPointCloud.setFont(font)
        self.ViewPointCloud.setObjectName("ViewPointCloud")
        self.horizontalLayoutWidget = QtWidgets.QWidget(PointCloudProject)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 341, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ManualRegistration = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ManualRegistration.sizePolicy().hasHeightForWidth())
        self.ManualRegistration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.ManualRegistration.setFont(font)
        self.ManualRegistration.setObjectName("ManualRegistration")
        self.horizontalLayout_2.addWidget(self.ManualRegistration)
        self.AutoRegistration = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutoRegistration.sizePolicy().hasHeightForWidth())
        self.AutoRegistration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.AutoRegistration.setFont(font)
        self.AutoRegistration.setObjectName("AutoRegistration")
        self.horizontalLayout_2.addWidget(self.AutoRegistration)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(PointCloudProject)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 341, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LoadDirectory = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadDirectory.sizePolicy().hasHeightForWidth())
        self.LoadDirectory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.LoadDirectory.setFont(font)
        self.LoadDirectory.setObjectName("LoadDirectory")
        self.horizontalLayout_3.addWidget(self.LoadDirectory)
        self.Deselect = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Deselect.sizePolicy().hasHeightForWidth())
        self.Deselect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.Deselect.setFont(font)
        self.Deselect.setObjectName("Deselect")
        self.horizontalLayout_3.addWidget(self.Deselect)
        self.label = QtWidgets.QLabel(PointCloudProject)
        self.label.setGeometry(QtCore.QRect(20, 190, 321, 16))
        self.label.setObjectName("label")
        self.CaptureData = QtWidgets.QPushButton(PointCloudProject)
        self.CaptureData.setGeometry(QtCore.QRect(20, 20, 321, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptureData.sizePolicy().hasHeightForWidth())
        self.CaptureData.setSizePolicy(sizePolicy)
        self.CaptureData.setObjectName("CaptureData")
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.ViewPointCloud.raise_()
        self.label.raise_()
        self.CaptureData.raise_()

        self.retranslateUi(PointCloudProject)
        QtCore.QMetaObject.connectSlotsByName(PointCloudProject)

    def retranslateUi(self, PointCloudProject):
        _translate = QtCore.QCoreApplication.translate
        PointCloudProject.setWindowTitle(_translate("PointCloudProject", "Point-Cloud-Project"))
        self.ViewPointCloud.setText(_translate("PointCloudProject", "View Point Cloud"))
        self.ManualRegistration.setText(_translate("PointCloudProject", "Manual Registration"))
        self.AutoRegistration.setText(_translate("PointCloudProject", "Auto Registration"))
        self.LoadDirectory.setText(_translate("PointCloudProject", "Load Directory"))
        self.Deselect.setText(_translate("PointCloudProject", "Deselect"))
        self.label.setText(_translate("PointCloudProject", "Directory selected:"))
        self.CaptureData.setText(_translate("PointCloudProject", "Capture Data"))
        self.LoadDirectory.clicked.connect(self.file_open)
        self.Deselect.clicked.connect(self.deselect)
        self.CaptureData.clicled.connect(self.CaptureDataForm)
        
    def file_open(self):
        dirName = QFileDialog.getExistingDirectory()
        self.label.setText("Directory Selected: " + dirName)
        self.Deselect.setEnabled(True)

    def deselect(self):
        dirName = " "
        self.label.setText("Directory Selected: " + dirName)
        self.Deselect.setEnabled(False)
    def CaptureDataForm(self):
        self.window=QtWidgets.QPointCloudProject()
        self.ui=Ui_MainWindow()
        self.ui=setupUi(self.window)
        PointCloudProject.hide()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PointCloudProject = QtWidgets.QDialog()
    ui = Ui_PointCloudProject()
    ui.setupUi(PointCloudProject)
    PointCloudProject.show()
    sys.exit(app.exec_())