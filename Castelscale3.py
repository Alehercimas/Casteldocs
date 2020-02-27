# Generate a set of Bezier curves in 3D space affected by some scaling factor

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def scale3m3(Pthr, Cpthr, xx, yy, zz):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    Pthfirst = Pthr[:-1]
    Pthlast = Pthr[1:]
    Pscales = np.zeros(6)
    Pthfull = np.hstack((Pthfirst, Cpthr, Pthlast))
    for i in Pthfull:
        j = scale3m2(i.reshape(-1,3), xx, yy, zz)
        ax.plot(j[:,0],j[:,1],j[:,2],'b')
        valtab = np.array([np.min(j[:,0]), np.max(j[:,0]), 
                           np.min(j[:,1]), np.max(j[:,1]), 
                           np.min(j[:,2]), np.max(j[:,2])])
        Pscales = np.vstack((Pscales, valtab))
    Pscales = Pscales[1:]
    xi = Pscales[:,0].min()
    xa = Pscales[:,1].max()
    yi = Pscales[:,2].min()
    ya = Pscales[:,3].max()
    zi = Pscales[:,4].min()
    za = Pscales[:,5].max()
    del Pscales
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
