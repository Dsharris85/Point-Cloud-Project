import os
import sys
import cv2
import shutil
import freenect 
import numpy as np
import frame_convert
import open3d as o3d

from tqdm import tqdm 
from calibkinect import *

total_taken = 1

def save_pcd(raw): 
    global total_taken

    dep = get_depth_arr_real_world(raw)

    print 'Saving to .pcd file...\n'

    header = """# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z
SIZE 4 4 4
TYPE F F F
COUNT 1 1 1
WIDTH {}
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS {}
DATA ascii
""".format( str(np.shape(dep)[0]),str(np.shape(dep)[0]))

    # write new file
    file_name = "{}/{}_cloud.pcd".format(dirName,total_taken)            
    pcd = open(file_name, "w")

    pcd.write(header)

    rows, cols = dep.shape
    count = 0
    to_write = ''

    for x in tqdm(range(rows)):

        x_coord = dep[x][0]
        y_coord = dep[x][1]
        z_coord = dep[x][2]

        to_write += "{} {} {}\n".format(x_coord,y_coord,z_coord)    
        
        count += 1

    pcd.write(to_write)
    pcd.close()
    print 'POINTS WRITTEN = {}'.format(str(count))
    print 'WRITTEN TO "{}"'.format(file_name)

    
# get depth image from kinect
def get_depth_arr_real_world(raw):
    return depth2xyzuv(raw)[0] 

def get_depth():
    return freenect.sync_get_depth(format=freenect.DEPTH_11BIT)[0] # format=freenect.DEPTH_11BIT

def get_depth_registered():
    return freenect.sync_get_depth(format=freenect.DEPTH_REGISTERED)[0]

def get_video():
    return frame_convert.video_cv(freenect.sync_get_video()[0])

def show():
    c = get_depth_registered()
    cv2.imshow('RGB', c)

def save_all():

    global total_taken

    # WRITE
    cv2.imwrite("{}/{}_rgb.png".format(dirName, total_taken), get_video())
    cv2.imwrite("{}/{}_depth_raw.png".format(dirName, total_taken), get_depth())
    cv2.imwrite("{}/{}_depth_registered.png".format(dirName, total_taken), get_depth_registered())
    cv2.imwrite("{}/{}_depth_pretty.png".format(dirName, total_taken), get_depth().astype(np.uint8))

    np.save("{}/raw_depth_{}".format(dirName, total_taken), get_depth())
    np.save("{}/registered_depth_{}".format(dirName, total_taken), get_depth_registered())

    save_pcd(get_depth())

    dep_reg = cv2.imread("{}/{}_depth_registered.png".format(dirName, total_taken))
    dep_raw = cv2.imread("{}/{}_depth_raw.png".format(dirName, total_taken))
    rgb_img = cv2.imread("{}/{}_rgb.png".format(dirName, total_taken))

    added_imgs = cv2.addWeighted(dep_reg, 0.9, rgb_img, 0.1, 0)
    added_imgs2 = cv2.addWeighted(dep_raw, 0.9, rgb_img, 0.1, 0)

    cv2.imwrite("{}/{}_overlayed_registered.png".format(dirName, total_taken), added_imgs)
    cv2.imwrite("{}/{}_overlayed_unregistered.png".format(dirName, total_taken), added_imgs2)

    total_taken += 1


################################################################
    
dirName = ''

if (len(sys.argv) > 1):
    dirName = sys.argv[1]
        
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("\nDirectory '{}' Created ".format(dirName))
    else:    
        print("\nDirectory '{}' already exists... ".format(dirName))
        yn = raw_input("\nOverwrite? (Y/N): ") 
        if(yn.lower() == "y"):
            shutil.rmtree(dirName)
            os.makedirs(dirName)
        else:
            print("\n\nExiting...")
            exit()
else:
    print("\nGive a new directory name... Exiting")
    exit() 


################################################################

cv2.namedWindow('RGB')

while 1:
    show()
    k = cv2.waitKey(30)
    if k == 32:#space    
        save_all()
        print '\n\nSaved!\n\n'
    
        pcd = o3d.io.read_point_cloud("{}/{}_cloud.pcd".format(dirName, total_taken - 1))
        o3d.visualization.draw_geometries([pcd])
    if k == 27:#esc
        break

#########################################################################



