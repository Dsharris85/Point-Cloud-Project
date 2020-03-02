import os
import sys
import time
import shutil
import datetime
import freenect 
import pyqtgraph
import threading 
import numpy as np
import pyqtgraph.opengl as gl

from tqdm import tqdm 
from calibkinect import *
from pyqtgraph.Qt import QtCore, QtGui 
from freenect import sync_get_depth as get_depth

total_taken = 1

# Inherting the base class 'Thread' 
# Used to help save .pcd file in background
class AsyncWrite(threading.Thread):  
  
    def __init__(self, dep): 
  
        # calling superclass init 
        threading.Thread.__init__(self)  
        self.dep = dep 
  
    def run(self): 
        global total_taken

        # write header
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
""".format( str(np.shape(self.dep)[0]),str(np.shape(self.dep)[0]))

        print 'Saving to .pcd file...\n'

        # write new file
        time = datetime.datetime.now()
        file_name = "{}/{}.pcd".format(dirName,total_taken)            
        pcd = open(file_name, "w")

        pcd.write(header)

        rows, cols = self.dep.shape
        count = 0
        to_write = ''

        # write points to file - later should add rgb data in
        # RGB = R << 16| G << 8 | B for .pcd filetypes
        for x in tqdm(range(rows)):

            x_coord = self.dep[x][0]
            y_coord = self.dep[x][1]
            z_coord = self.dep[x][2]

            # add to string then write one big string to file rather than write each point to file at a time
            to_write += "{} {} {}\n".format(x_coord,y_coord,z_coord)    
            
            count += 1

        pcd.write(to_write)
        pcd.close()
        print 'COORDS WRITTEN = {}'.format(str(count))
        print 'WRITTEN TO "{}"'.format(file_name)
        total_taken += 1
        

paused = False

# Inherit from GLVW to override for custom keyboard events
class MyView(gl.GLViewWidget):
    def keyPressEvent(self, ev):
        global paused, depth_arr

        ctx = freenect.init()
        dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)

        # SPACEBAR to 'pause' and 'unpause'
        if (ev.key() == 32 and paused):
            t.start(10)
            paused = False
        elif (ev.key() == 32):
            t.stop()
            paused = True
        # 'S' key to save curr frame to .pcd
        elif (ev.key() == 83):
            background = AsyncWrite(depth_arr) 
            background.start() 
       

# get depth image from kinect
def get_depth_arr():
    return depth2xyzuv(get_depth()[0])[0] 

# return random depth array shape == (50k,3)
def get_rand_arr():
    arr_test =[]    
    return np.random.randint(-3000,-2000,size=(50000,3))

i = 0
def update():
    global sp2, move, i, depth_arr

    # clear screen and add new cloud
    try:
        w.removeItem(sp2)
    except:
        print 'OH NO LOL... fix me'

    downsample = 2
    
    # plot data
    depth_arr = get_depth_arr()
    sp2 = gl.GLScatterPlotItem(pos=depth_arr[::downsample], size=2, color=pyqtgraph.glColor((i, 50 * 1.3)), pxMode=True)

    w.addItem(sp2)
    i += 1
    
dirName = ''

if (len(sys.argv) > 1):
    dirName = sys.argv[1]
        
    # file handling - makes new if not there, else asks for overwrite
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


# start/show
app = QtGui.QApplication([])
w = MyView()
w.show()

# initial arr is random plots
depth_arr = get_rand_arr()

# params
w.opts['distance'] = 500
w.opts['fov'] = 1
w.pan(0, 0, 0, relative=False)

# set-up title grid etc...
w.setWindowTitle('Kinect Point Cloud')

# X axis
x_ax = gl.GLLinePlotItem()
x_ax.setData(pos=np.array([[0,0,0],[1000,0,0]]),width=2,antialias=True, color=pyqtgraph.glColor((255,0,0)))
w.addItem(x_ax)
# Y axis
y_ax = gl.GLLinePlotItem()
y_ax.setData(pos=np.array([[0,0,0],[0,1000,0]]),width=2,antialias=True, color=pyqtgraph.glColor((0,255,0)))
w.addItem(y_ax)
# Z axis
z_ax = gl.GLLinePlotItem()
z_ax.setData(pos=np.array([[0,0,0],[0,0,1000]]),width=2,antialias=True, color=pyqtgraph.glColor((0,0,255)))
w.addItem(z_ax)
z2_ax = gl.GLLinePlotItem()
z2_ax.setData(pos=np.array([[0,0,0],[0,0,-2000]]),width=1,antialias=True, color=pyqtgraph.glColor((0,0,200)))
w.addItem(z2_ax)

# init with random points - keep regardless of kinect/no kinect
pos = np.random.randint(-3000,-2000,size=(500,3))
sp2 = gl.GLScatterPlotItem(pos=get_rand_arr())

# init plot
sp2 = gl.GLScatterPlotItem(pos=pos,size=6, pxMode=True) 
sp2.setGLOptions('opaque')
w.addItem(sp2)

# start timer and connect to update func
t = QtCore.QTimer()
t.timeout.connect(update)
t.start(10)


if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
