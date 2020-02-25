# Generate a set of Bezier curves in 3D space

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def castelsim3d(Pthr, Cpthr):
    #fig = plt.figure()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    Pthfirst = Pthr[:-1] # Create the "P0" control points from P
    Pthlast = Pthr[1:] # Create the "PN" control points from P
    Pthfull = np.hstack((Pthfirst, Cpthr, Pthlast)) # Combine the control points
    for i in Pthfull:
        j = castest3d(i.reshape(-1,3)) # Works out a Curve for each row
        ax.plot(j[:,0],j[:,1],j[:,2],'b') # The X, Y and Z axes that will be used
    plt.show()
