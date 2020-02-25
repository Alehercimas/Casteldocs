# 3D Rotation Matrix in the x direction taking an array of size 3

import numpy as np

def rot3x(coor, th):
    # The rotation matrix itself
    rott = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], 
                     [0, np.sin(th), np.cos(th)]])
    coor = coor[:,np.newaxis] # Make the shape vertical
    coor = rott @ coor # Matrix multiplication
    coor = coor[:,0] # Return to horizontal shape
    return coor
