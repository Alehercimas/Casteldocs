# Rotation Matrix function taking as inputs some array of size 2 (x,y) and the angle theta (th)

import numpy as np

def rot(coor, th):
    # The rotation matrix itself
    rott = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    coor = coor[:,np.newaxis] # Make the shape vertical
    coor = rott @ coor # Matrix multiplication
    coor = coor[:,0] # Return to horizontal shape
    return coor
