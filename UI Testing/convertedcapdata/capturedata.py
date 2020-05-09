# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capturedata.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureForm(object):
    def setupUi(self, CaptureForm):
        CaptureForm.setObjectName("CaptureForm")
        CaptureForm.resize(299, 327)
        self.verticalLayout = QtWidgets.QVBoxLayout(CaptureForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CaptureFrames = QtWidgets.QPushButton(CaptureForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptureFrames.sizePolicy().hasHeightForWidth())
        self.CaptureFrames.setSizePolicy(sizePolicy)
        self.CaptureFrames.setCheckable(True)
        self.CaptureFrames.setChecked(False)
        self.CaptureFrames.setObjectName("CaptureFrames")
        self.horizontalLayout.addWidget(self.CaptureFrames)
        self.Exit = QtWidgets.QPushButton(CaptureForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Exit.sizePolicy().hasHeightForWidth())
        self.Exit.setSizePolicy(sizePolicy)
        self.Exit.setObjectName("Exit")
        self.horizontalLayout.addWidget(self.Exit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.VideoFeed = QtWidgets.QLabel(CaptureForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoFeed.sizePolicy().hasHeightForWidth())
        self.VideoFeed.setSizePolicy(sizePolicy)
        self.VideoFeed.setMinimumSize(QtCore.QSize(255, 255))
        self.VideoFeed.setText("")
        self.VideoFeed.setObjectName("VideoFeed")
        self.verticalLayout_2.addWidget(self.VideoFeed)
        self.line = QtWidgets.QFrame(CaptureForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.ImagesTaken = QtWidgets.QLabel(CaptureForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagesTaken.sizePolicy().hasHeightForWidth())
        self.ImagesTaken.setSizePolicy(sizePolicy)
        self.ImagesTaken.setAutoFillBackground(False)
        self.ImagesTaken.setFrameShape(QtWidgets.QFrame.Box)
        self.ImagesTaken.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ImagesTaken.setLineWidth(0)
        self.ImagesTaken.setMidLineWidth(0)
        self.ImagesTaken.setObjectName("ImagesTaken")
        self.verticalLayout_2.addWidget(self.ImagesTaken)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MaxImages = QtWidgets.QLabel(CaptureForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MaxImages.sizePolicy().hasHeightForWidth())
        self.MaxImages.setSizePolicy(sizePolicy)
        self.MaxImages.setFrameShape(QtWidgets.QFrame.Box)
        self.MaxImages.setObjectName("MaxImages")
        self.horizontalLayout_2.addWidget(self.MaxImages)
        self.progressBar = QtWidgets.QProgressBar(CaptureForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(CaptureForm)
        QtCore.QMetaObject.connectSlotsByName(CaptureForm)

    def retranslateUi(self, CaptureForm):
        _translate = QtCore.QCoreApplication.translate
        CaptureForm.setWindowTitle(_translate("CaptureForm", "Capture Data"))
        self.CaptureFrames.setText(_translate("CaptureForm", "Capture Frames"))
        self.Exit.setText(_translate("CaptureForm", "Exit"))
        self.ImagesTaken.setText(_translate("CaptureForm", "Images Taken: "))
        self.MaxImages.setText(_translate("CaptureForm", " Max 1500 Images "))
        self.progressBar.setFormat(_translate("CaptureForm", "%p%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaptureForm = QtWidgets.QWidget()
    ui = Ui_CaptureForm()
    ui.setupUi(CaptureForm)
    CaptureForm.show()
    sys.exit(app.exec_())

