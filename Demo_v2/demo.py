import time
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

# Inherting the base class 'Thread' 
# Used to help save .pcd file in background
class AsyncWrite(threading.Thread):  
  
    def __init__(self, dep): 
  
        # calling superclass init 
        threading.Thread.__init__(self)  
        self.dep = dep 
  
    def run(self): 
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
        file_name = "PCD/KINECT_CLOUD_{}.pcd".format(time)            
        pcd = open(file_name, "w")

        rows, cols = self.dep.shape
        count = 0
        to_write = ''

        for x in tqdm(range(rows)):

            x_coord = self.dep[x][0]
            y_coord = self.dep[x][1]
            z_coord = self.dep[x][2]

            to_write += "{} {} {}\n".format(x_coord,y_coord,z_coord)    
            
            count += 1

        pcd.write(to_write)
        pcd.close()
        print 'COORDS WRITTEN = {}'.format(str(count))
        print 'WRITTEN TO "{}"'.format(file_name)


paused = False

# Inherit from GLVW to override for custom keyboard events
class MyView(gl.GLViewWidget):
    def keyPressEvent(self, ev):
        global paused, depth_arr

        #print ev.key()

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
        print 'OH NO LOL'

    # KINECT DATA -- uncomment if using kinect, otherwise use random points
    #kin_arr = get_depth_arr()
    #sp2 = gl.GLScatterPlotItem(pos=kin_arr[::4], size=2, color=pyqtgraph.glColor((i, 50 * 1.3)), pxMode=True)

    # RANDOM DATA -- uncomment if no kinect, uses randomly generated points. Comment out if using kinect
    depth_arr = get_rand_arr()[::4]
    # feel free to remove color parameter if too much an eyesore
    sp2 = gl.GLScatterPlotItem(pos=depth_arr, size=2, color=pyqtgraph.glColor((i, 50 * 1.3)), pxMode=True) 
    sp2.translate(2500,2500,2500)

    w.addItem(sp2)
    i += 1

# start/show
app = QtGui.QApplication([])
w = MyView()
w.show()

depth_arr = get_rand_arr()

# params
w.opts['distance'] = 3000
w.opts['elevation'] = -90 
w.opts['fov'] = 1
w.pan(630, 350, 0, relative=False)

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
