import os
import sys
import shutil
import cv2
import freenect 
import numpy as np
import frame_convert
import open3d as o3d

from updateJson import *

# global counter, counts how many images taken (for naming scheme)
total_taken = 1

print("test")

def get_depth_registered():
    return freenect.sync_get_depth(format=freenect.DEPTH_REGISTERED)[0]

def get_video():
    return frame_convert.video_cv(freenect.sync_get_video()[0])

def show(saved):
    img = np.array(get_video())

    font = cv2.FONT_HERSHEY_SIMPLEX
    pos = (10,20)
    fontScale = 0.5
    fontColor = (255,255,255)
    lineType = 1

    img = cv2.rectangle(img, (0,0), (420,60), (20,20,20), -1)   # box
    img = cv2.rectangle(img, (0,0), (420,60), (255,255,255), 1) # border
    cv2.putText(img,'Press \'Space\' to capture frame and \'Esc\' to exit', # text
        pos, 
        font, 
        fontScale,
        fontColor,
        lineType)
    cv2.putText(img,'Images Taken: {}'.format(saved), # text for counter
        (10,45), 
        font, 
        fontScale,
        fontColor,
        lineType)   
    cv2.imshow('RGB', img)

def save_all(d):
    global total_taken
    dirName = d
    
    # save depth/rgb aligned images
    cv2.imwrite("{}/color/{}.jpg".format(dirName, str(total_taken).zfill(6)), get_video())
    cv2.imwrite("{}/depth/{}.png".format(dirName, str(total_taken).zfill(6)), get_depth_registered())

    total_taken += 1
    
    print("Saved capture {} to {}!".format(total_taken, dirName))

def main_capture(d):

    updateConfig(d)

    print("test - main capture")
    cv2.startWindowThread()
    cv2.namedWindow('RGB')

    print('hi')
    flag = True
    saving = 0
    
    print("test - main capture2")

    while (flag):
        show(saving)
        if (saving != 0): 
            save_all(d)
            saving +=1       
        k = cv2.waitKey(30)
        if k == 32:#space    
            saving += 1
        if k == 27 or saving > 1500: # esc/limit on 1500 saved
            flag = False

    # clean up
    cv2.destroyAllWindows()
    freenect.sync_stop()
