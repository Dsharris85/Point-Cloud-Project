# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptureDataEdited.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureData(object):
    def setupUi(self, CaptureData):
        CaptureData.setObjectName("CaptureData")
        CaptureData.resize(448, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CaptureData.sizePolicy().hasHeightForWidth())
        CaptureData.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CaptureData)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LoadDir_3 = QtWidgets.QPushButton(CaptureData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadDir_3.sizePolicy().hasHeightForWidth())
        self.LoadDir_3.setSizePolicy(sizePolicy)
        self.LoadDir_3.setObjectName("LoadDir_3")
        self.horizontalLayout_4.addWidget(self.LoadDir_3)
        self.Deselect = QtWidgets.QPushButton(CaptureData)
        self.Deselect.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Deselect.sizePolicy().hasHeightForWidth())
        self.Deselect.setSizePolicy(sizePolicy)
        self.Deselect.setObjectName("Deselect")
        self.horizontalLayout_4.addWidget(self.Deselect)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CaptureData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(CaptureData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(CaptureData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.DirText = QtWidgets.QLabel(CaptureData)
        self.DirText.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DirText.sizePolicy().hasHeightForWidth())
        self.DirText.setSizePolicy(sizePolicy)
        self.DirText.setText("")
        self.DirText.setObjectName("DirText")
        self.verticalLayout_2.addWidget(self.DirText)

        self.retranslateUi(CaptureData)
        QtCore.QMetaObject.connectSlotsByName(CaptureData)

    def retranslateUi(self, CaptureData):
        _translate = QtCore.QCoreApplication.translate
        CaptureData.setWindowTitle(_translate("CaptureData", "PointCloudProject"))
        self.LoadDir_3.setText(_translate("CaptureData", "Load Directory"))
        self.Deselect.setText(_translate("CaptureData", "Deselect"))
        self.label.setText(_translate("CaptureData", " Enter a Directory Name:"))
        self.pushButton.setText(_translate("CaptureData", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaptureData = QtWidgets.QDialog()
    ui = Ui_CaptureData()
    ui.setupUi(CaptureData)
    CaptureData.show()
    sys.exit(app.exec_())

