# Generate a set of Bezier curves in 3D space, axes reshaped so the graph has actual proportions 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def castelsim3d(Pthr, Cpthr, Bounds=False):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    Pthfirst = Pthr[:-1] # Create the "P0" control points from P
    Pthlast = Pthr[1:] # Create the "PN" control points from P
    Pthfull = np.hstack((Pthfirst, Cpthr, Pthlast)) # Combine the control points
    for i in Pthfull:
        j = castest3d(i.reshape(-1,3)) # Works out a Curve for each row
        ax.plot(j[:,0],j[:,1],j[:,2],'b') # The X, Y and Z axes that will be used
    # work out a "bounding square" of sorts to keep the data proportional
    xi, xa = Pthr[:,0].min(), Pthr[:,0].max()
    yi, ya = Pthr[:,1].min(), Pthr[:,1].max()
    zi, za = Pthr[:,2].min(), Pthr[:,2].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    # An array of points for the corners of my plots
    endpoints = np.array([
            [centre[0] - line, centre[1] - line, centre[2] - line], 
            [centre[0] - line, centre[1] - line, centre[2] + line], 
            [centre[0] - line, centre[1] + line, centre[2] - line], 
            [centre[0] - line, centre[1] + line, centre[2] + line], 
            [centre[0] + line, centre[1] - line, centre[2] - line], 
            [centre[0] + line, centre[1] - line, centre[2] + line], 
            [centre[0] + line, centre[1] + line, centre[2] - line], 
            [centre[0] + line, centre[1] + line, centre[2] + line]])
    # If true, you see the points on the plot
    if Bounds is True:
        ax.scatter(endpoints[:,0],endpoints[:,1],endpoints[:,2],'b')
    
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    
    plt.show()
