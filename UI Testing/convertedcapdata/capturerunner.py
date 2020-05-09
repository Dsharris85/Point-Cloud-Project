from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os.path
import sys
import threading

# testing import
import time

# imports for layout
from capturedata import Ui_CaptureForm

# imports for functionality
import cv2
# import freenect 
# import numpy as np
# import frame_convert
# from updateJson import *

# global for capture ensures program does not exit until capture is finished
capture_on = 0
# global counter, counts how many images were taken
total_taken = 0

# def get_depth_registered():
#     return freenect.sync_get_depth(format=freenect.DEPTH_REGISTERED)[0]

# def get_video():
#     return frame_convert.video_cv(freenect.sync_get_video()[0])

class VideoThread(QtCore.QThread):
    update_video = QtCore.pyqtSignal(QtGui.QImage)

    def run(self):
        #while True:
            print("hello")
        #    img = np.array(get_video())
            img = cv2.imread('pikachu.PNG')
            img = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            img = img.scaled(300, 300, QtCore.Qt.KeepAspectRatio)

            self.update_video.emit(img)

class CaptureThread(QtCore.QThread):
    update_total = QtCore.pyqtSignal()
    
    def __init__(self, dirName):
        super().__init__()
        self.dirName = dirName
    
    def run(self):
        global total_taken
        while (capture_on) and (total_taken < 1500):
            time.sleep(0.001) # for testing

            #cv2.imwrite("{}/color/{}.jpg".format(self.dirName, str(total_taken).zfill(6)), get_video())
            #cv2.imwrite("{}/depth/{}.png".format(self.dirName, str(total_taken).zfill(6)), get_depth_registered())

            total_taken += 1
            self.update_total.emit()

# Class handling for capture data form
class CaptureForm(QtWidgets.QDialog):
    def __init__(self, givendirName):
        super(CaptureForm, self).__init__()
        self.ui = Ui_CaptureForm()
        self.ui.setupUi(self)
        self.show()
        self.dirName = givendirName

        self.videothread = VideoThread()
        self.videothread.update_video.connect(self.update_video)
        self.videothread.start()

        self.ui.CaptureFrames.clicked.connect(self.capframes)
        self.ui.Exit.clicked.connect(self.exitcapture)
        self.ui.closeEvent = self.closeEvent # To avoid incomplete captures

    def update_video(self, image):
        self.ui.VideoFeed.setPixmap(QtGui.QPixmap.fromImage(image))

    def capframes(self):
        global capture_on
        if(self.ui.CaptureFrames.isChecked()):
            capture_on = 1
            self.capturethread = CaptureThread(self.dirName)
            self.capturethread.update_total.connect(self.update_total)
            self.capturethread.start()
        else:
            capture_on = 0
            self.capturethread.wait()

    def update_total(self):
        self.ui.ImagesTaken.setText("Images Taken: {}".format(total_taken))
        self.ui.progressBar.setValue(total_taken/1500 * 100)

        if (total_taken == 1500):  
            self.ui.CaptureFrames.click()
            self.ui.CaptureFrames.setEnabled(False)

    def exitcapture(self):
        self.close()

    def closeEvent(self, event):
        global video_on
        global capture_on
        video_on = 0
        capture_on = 0
        self.videothread.quit()
        self.accept()



if __name__ == "__main__":
    sampledirName = "C:\\Kenjisayshi!"
    # updateConfig(sampledirName)
    app = QtWidgets.QApplication(sys.argv)
    Form = CaptureForm(sampledirName)
    sys.exit(app.exec_())
