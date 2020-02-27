# Bringing all my 3D rotation and "de Casteljau" functions together.
# Rotating a particular set of bezier curves in x, y or z direction (n-1) amount of times
# Created and bound to a specific scale

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def Castellan(Points, Controlpoints, Axes, Thetnums=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    Pirange = np.linspace(0,np.pi*2,Thetnums)
    Pscales = np.zeros(6)
    Pointfirst = Points[:-1]
    Pointlast = Points[1:]
    Pointfull = np.hstack((Pointfirst, Controlpoints, Pointlast))
    if Axes == 'x':
        for i in Pirange:
            for j in Pointfull:
                k = castestrot3x(j.reshape(-1,3), i)
                ax.plot(k[:,0],k[:,1],k[:,2],'b')
                valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                   np.min(k[:,1]), np.max(k[:,1]), 
                                   np.min(k[:,2]), np.max(k[:,2])])
                Pscales = np.vstack((Pscales, valtab))
    elif Axes == 'y':
        for i in Pirange:
            for j in Pointfull:
                k = castestrot3y(j.reshape(-1,3), i)
                ax.plot(k[:,0],k[:,1],k[:,2],'b')
                valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                   np.min(k[:,1]), np.max(k[:,1]), 
                                   np.min(k[:,2]), np.max(k[:,2])])
                Pscales = np.vstack((Pscales, valtab))
    elif Axes == 'z':
        for i in Pirange:
            for j in Pointfull:
                k = castestrot3z(j.reshape(-1,3), i)
                ax.plot(k[:,0],k[:,1],k[:,2],'b')
                valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                   np.min(k[:,1]), np.max(k[:,1]), 
                                   np.min(k[:,2]), np.max(k[:,2])])
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
