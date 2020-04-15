import os
import sys
import shutil
import cv2
import freenect 
import numpy as np
import frame_convert
import open3d as o3d

from tqdm import tqdm 

total_taken = 1

def get_depth_registered():
    return freenect.sync_get_depth(format=freenect.DEPTH_REGISTERED)[0]

def get_video():
    return frame_convert.video_cv(freenect.sync_get_video()[0])

def show():
    img = np.array(get_video())

    font = cv2.FONT_HERSHEY_SIMPLEX
    pos = (10,20)
    fontScale = 0.5
    fontColor = (255,255,255)
    lineType = 1

    img = cv2.rectangle(img, (0,0), (420,30), (20,20,20), -1)   # box
    img = cv2.rectangle(img, (0,0), (420,30), (255,255,255), 1) # border
    cv2.putText(img,'Press \'Space\' to capture frame and \'Esc\' to exit', # text
        pos, 
        font, 
        fontScale,
        fontColor,
        lineType)

    cv2.imshow('RGB', img)

def save_all(d):
    global total_taken
    dirName = d
    
    # save depth/rgb aligned images
    cv2.imwrite("{}/{}_rgb.jpg".format(dirName, total_taken), get_video())
    cv2.imwrite("{}/{}_depth_registered.png".format(dirName, total_taken), get_depth_registered())

    total_taken += 1
    
    print("Saved capture {} to {}!".format(total_taken, dirName))

def main_capture(d):
    cv2.namedWindow('RGB')
    flag = True

    while (flag):
        show()
        k = cv2.waitKey(30)
        if k == 32:#space    
            save_all(d)
        if k == 27:#esc
            flag = False
    cv2.destroyAllWindows()

