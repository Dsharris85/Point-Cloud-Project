# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptureDataWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaptureData(object):
    def setupUi(self, CaptureData):
        CaptureData.setObjectName("CaptureData")
        CaptureData.resize(301, 220)
        self.centralwidget = QtWidgets.QWidget(CaptureData)
        self.centralwidget.setObjectName("centralwidget")
        self.CaptureDataForm = QtWidgets.QGroupBox(self.centralwidget)
        self.CaptureDataForm.setGeometry(QtCore.QRect(10, 10, 281, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptureDataForm.sizePolicy().hasHeightForWidth())
        self.CaptureDataForm.setSizePolicy(sizePolicy)
        self.CaptureDataForm.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptureDataForm.setObjectName("CaptureDataForm")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.CaptureDataForm)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(250, 70, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_2.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_2.setSizePolicy(sizePolicy)
        self.commandLinkButton_2.setText("")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CaptureDataForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 281, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fromanexistingDirectory = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromanexistingDirectory.sizePolicy().hasHeightForWidth())
        self.fromanexistingDirectory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.fromanexistingDirectory.setFont(font)
        self.fromanexistingDirectory.setObjectName("fromanexistingDirectory")
        self.horizontalLayout.addWidget(self.fromanexistingDirectory)
        self.Deselect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Deselect.sizePolicy().hasHeightForWidth())
        self.Deselect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.Deselect.setFont(font)
        self.Deselect.setObjectName("Deselect")
        self.horizontalLayout.addWidget(self.Deselect)
        self.DirText = QtWidgets.QLabel(self.CaptureDataForm)
        self.DirText.setEnabled(False)
        self.DirText.setGeometry(QtCore.QRect(0, 140, 291, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DirText.sizePolicy().hasHeightForWidth())
        self.DirText.setSizePolicy(sizePolicy)
        self.DirText.setObjectName("DirText")
        self.label = QtWidgets.QLabel(self.CaptureDataForm)
        self.label.setGeometry(QtCore.QRect(0, 60, 211, 21))
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
        self.text = QtWidgets.QPlainTextEdit(self.CaptureDataForm)
        self.text.setGeometry(QtCore.QRect(0, 80, 251, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.text.setFont(font)
        self.text.setStyleSheet("border-top-color: rgb(85, 0, 0);\n"
"border-right-color: rgb(85, 0, 0);\n"
"border-bottom-color: rgb(85, 0, 0);\n"
"border-left-color: rgb(85, 0, 0);")
        self.text.setPlainText("")
        self.text.setObjectName("text")
        self.backtomainmenu = QtWidgets.QPushButton(self.CaptureDataForm)
        self.backtomainmenu.setGeometry(QtCore.QRect(0, 110, 251, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backtomainmenu.sizePolicy().hasHeightForWidth())
        self.backtomainmenu.setSizePolicy(sizePolicy)
        self.backtomainmenu.setObjectName("backtomainmenu")
        CaptureData.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaptureData)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.menubar.setObjectName("menubar")
        CaptureData.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaptureData)
        self.statusbar.setObjectName("statusbar")
        CaptureData.setStatusBar(self.statusbar)

        self.retranslateUi(CaptureData)
        QtCore.QMetaObject.connectSlotsByName(CaptureData)

    def retranslateUi(self, CaptureData):
        _translate = QtCore.QCoreApplication.translate
        CaptureData.setWindowTitle(_translate("CaptureData", "PointCloudProject"))
        self.CaptureDataForm.setTitle(_translate("CaptureData", "Capture Data"))
        self.fromanexistingDirectory.setText(_translate("CaptureData", "From an Existing Directory"))
        self.Deselect.setText(_translate("CaptureData", "Deselect"))
        self.DirText.setText(_translate("CaptureData", "Directory Selected:"))
        self.label.setText(_translate("CaptureData", "Enter a Directory Name:"))
        self.backtomainmenu.setText(_translate("CaptureData", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaptureData = QtWidgets.QMainWindow()
    ui = Ui_CaptureData()
    ui.setupUi(CaptureData)
    CaptureData.show()
    sys.exit(app.exec_())