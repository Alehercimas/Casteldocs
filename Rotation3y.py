# 3D Rotation Matrix in the y direction taking an array of size 3

import numpy as np

def rot3y(coor, th):
    # The rotation matrix itself
    rott = np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], 
                      [-np.sin(th), 0, np.cos(th)]])
    coor = coor[:,np.newaxis] # Make the shape vertical
    coor = rott @ coor # Matrix multiplication
    coor = coor[:,0] # Return to horizontal shape
    return coor
