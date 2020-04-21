# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(353, 192)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CaptureDataForm = QtWidgets.QGroupBox(self.centralwidget)
        self.CaptureDataForm.setGeometry(QtCore.QRect(10, 10, 341, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptureDataForm.sizePolicy().hasHeightForWidth())
        self.CaptureDataForm.setSizePolicy(sizePolicy)
        self.CaptureDataForm.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptureDataForm.setObjectName("CaptureDataForm")
        self.FromanexistingDirectory = QtWidgets.QPushButton(self.CaptureDataForm)
        self.FromanexistingDirectory.setGeometry(QtCore.QRect(10, 30, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FromanexistingDirectory.sizePolicy().hasHeightForWidth())
        self.FromanexistingDirectory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.FromanexistingDirectory.setFont(font)
        self.FromanexistingDirectory.setObjectName("FromanexistingDirectory")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.CaptureDataForm)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 90, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("border-top-color: rgb(85, 0, 0);\n"
"border-right-color: rgb(85, 0, 0);\n"
"border-bottom-color: rgb(85, 0, 0);\n"
"border-left-color: rgb(85, 0, 0);")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.CaptureDataForm)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Deselect_2 = QtWidgets.QPushButton(self.CaptureDataForm)
        self.Deselect_2.setGeometry(QtCore.QRect(180, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.Deselect_2.setFont(font)
        self.Deselect_2.setObjectName("Deselect_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.CaptureDataForm)
        self.commandLinkButton.setGeometry(QtCore.QRect(290, 90, 31, 31))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.plainTextEdit.raise_()
        self.FromanexistingDirectory.raise_()
        self.label_2.raise_()
        self.Deselect_2.raise_()
        self.commandLinkButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CaptureDataForm.setTitle(_translate("MainWindow", "Capture Data"))
        self.FromanexistingDirectory.setText(_translate("MainWindow", "From an Existing Directory"))
        self.label_2.setText(_translate("MainWindow", "From Entering a Directory Name:"))
        self.Deselect_2.setText(_translate("MainWindow", "Deselect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())