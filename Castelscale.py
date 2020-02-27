# Scaling matrix

import numpy as np

def scale3m(coor, x, y, z):
    # The scaling matrix itself
    scal = np.array([[x, 0, 0], [0, y, 0], [0, 0, z]])
    coor = coor[:,np.newaxis] # Make the shape vertical
    coor = scal @ coor # Matrix multiplication
    coor = coor[:,0] # Return to horizontal shape
    return coor
