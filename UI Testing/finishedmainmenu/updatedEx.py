# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatedEx.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainMenu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(309, 220)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CaptureData = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptureData.sizePolicy().hasHeightForWidth())
        self.CaptureData.setSizePolicy(sizePolicy)
        self.CaptureData.setObjectName("CaptureData")
        self.verticalLayout.addWidget(self.CaptureData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Reg = QtWidgets.QPushButton(Dialog)
        self.Reg.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Reg.sizePolicy().hasHeightForWidth())
        self.Reg.setSizePolicy(sizePolicy)
        self.Reg.setObjectName("Reg")
        self.horizontalLayout_2.addWidget(self.Reg)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoadDir = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadDir.sizePolicy().hasHeightForWidth())
        self.LoadDir.setSizePolicy(sizePolicy)
        self.LoadDir.setObjectName("LoadDir")
        self.horizontalLayout.addWidget(self.LoadDir)
        self.Deselect = QtWidgets.QPushButton(Dialog)
        self.Deselect.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Deselect.sizePolicy().hasHeightForWidth())
        self.Deselect.setSizePolicy(sizePolicy)
        self.Deselect.setObjectName("Deselect")
        self.horizontalLayout.addWidget(self.Deselect)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.DirText = QtWidgets.QLabel(Dialog)
        self.DirText.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DirText.sizePolicy().hasHeightForWidth())
        self.DirText.setSizePolicy(sizePolicy)
        self.DirText.setObjectName("DirText")
        self.verticalLayout.addWidget(self.DirText)
        self.ViewPointCloud = QtWidgets.QPushButton(Dialog)
        self.ViewPointCloud.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewPointCloud.sizePolicy().hasHeightForWidth())
        self.ViewPointCloud.setSizePolicy(sizePolicy)
        self.ViewPointCloud.setObjectName("ViewPointCloud")
        self.verticalLayout.addWidget(self.ViewPointCloud)
        self.ViewMesh = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewMesh.sizePolicy().hasHeightForWidth())
        self.ViewMesh.setSizePolicy(sizePolicy)
        self.ViewMesh.setObjectName("ViewMesh")
        self.verticalLayout.addWidget(self.ViewMesh)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PointCloudProject"))
        self.CaptureData.setText(_translate("Dialog", "Capture Data"))
        self.Reg.setText(_translate("Dialog", "Registration"))
        self.LoadDir.setText(_translate("Dialog", "Load Directory"))
        self.Deselect.setText(_translate("Dialog", "Deselect"))
        self.DirText.setText(_translate("Dialog", "Directory Selected:"))
        self.ViewPointCloud.setText(_translate("Dialog", "View Point Cloud"))
        self.ViewMesh.setText(_translate("Dialog", "View Mesh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainMenu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

