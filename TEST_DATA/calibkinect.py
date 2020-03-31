#   Edited version of : https://github.com/amiller/libfreenect-goodies/blob/master/calibkinect.py

import numpy as np

scaler = 0.001
theta = 0
  
# Return real-world coords from raw kinect depth data 
# Depth values returned should be in meters
def depth2xyzuv(depth, u=None, v=None):
  transl = 0

  if u is None or v is None:
    u,v = np.mgrid[:480,:640]
  
  # RGB = R << 16| G << 8 | B

  # Build a 3xN matrix of the d,u,v data
  C = np.vstack((u.flatten(), v.flatten(), depth.flatten(), 0*u.flatten()+1))

  # Project the duv matrix into xyz using xyz_matrix()
  X,Y,Z,W = np.dot(xyz_matrix(),C)
  X,Y,Z = ((Y/W) * scaler), ((X/W) * scaler), ((Z/W) * scaler )#* -1.0) - 500  #+ 2048
  xyz = np.vstack((X,Y,Z)).transpose()
  xyz = xyz[Z<0,:]

  # Project the duv matrix into U,V rgb coordinates using rgb_matrix() and xyz_matrix()
  U,V,_,W = np.dot(np.dot(uv_matrix(), xyz_matrix()),C)
  U,V = U/W, V/W
  uv = np.vstack((U,V)).transpose()    
  uv = uv[Z<0,:]       

  # Return both the XYZ coordinates and the UV coordinates
  # Only using XYZ currently
  return xyz, uv

def rotate(X, theta, axis='x'):
  c, s = np.cos(theta), np.sin(theta)
  if axis == 'x': return np.dot(X, np.array([
    [1.,  0,  0],
    [0 ,  c, -s],
    [0 ,  s,  c]
  ]))
  elif axis == 'y': return np.dot(X, np.array([
    [c,  0,  -s],
    [0,  1,   0],
    [s,  0,   c]
  ]))
  elif axis == 'z': return np.dot(X, np.array([
    [c, -s,  0 ],
    [s,  c,  0 ],
    [0,  0,  1.],
  ]))

def uv_matrix():
  rot = np.array([[ 9.99846e-01,   -1.26353e-03,   1.74872e-02], 
                  [-1.4779096e-03, -9.999238e-01,  1.225138e-02],
                  [1.747042e-02,   -1.227534e-02,  -9.99772e-01]])
  trans = np.array([[1.9985e-02, -7.44237e-04,-1.0916736e-02]])
  m = np.hstack((rot, -trans.transpose()))
  m = np.vstack((m, np.array([[0,0,0,1]])))
  KK = np.array([[529.2, 0, 329, 0],
                 [0, 525.6, 267.5, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])
  m = np.dot(KK, (m))
  return m


def xyz_matrix():
  fx = 594.21
  fy = 591.04
  a = -0.0030711
  b = 3.3309495
  cx = 339.5
  cy = 242.7

  mat = np.array([[1/fx, 0, 0, -cx/fx],
                  [0, -1/fy, 0, cy/fy],
                  [0,   0, 0,    -1],
                  [0,   0, a,     b]])
  return mat
