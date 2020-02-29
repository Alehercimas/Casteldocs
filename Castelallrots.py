# Various functions for computing a set of Bezier curves rotated around all three axes multiple times

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Rotation matrices in x, y and z directions respectively
def rotx(th):
    rotx = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], 
                     [0, np.sin(th), np.cos(th)]])
    return rotx

def roty(th):
    roty = np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], 
                      [-np.sin(th), 0, np.cos(th)]])
    return roty

def rotz(th):
    rotz = np.array([[np.cos(th), -np.sin(th), 0], 
                      [np.sin(th), np.cos(th), 0], [0, 0, 1]])
    return rotz

def operation(coor, trn):
    rott = trn
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

# A function using all rotation matrices 
def rotthr(oldarr, xtht, ytht, ztht):
    pp = np.hstack((oldarr[:-1], oldarr[1:]))
    a, b = np.shape(oldarr)
    c = np.arange(a - 2)
    t = np.linspace(0,1,11)
    p = np.array([0,0,0])
    newarr = np.array([0,0,0])
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-3]) + (h*j[3:]))).reshape(-1,3)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0,0])
        newarr = np.append(newarr, 
                           (((1-h)*pp[:,:-3]) + (h*pp[:,3:]))).reshape(-1,3)
        pp = np.hstack((oldarr[:-1], oldarr[1:]))
    newarr = newarr[1:]
    a, b = np.shape(newarr)
    a = np.arange(a)
    rottot = rotx(xtht) @ roty(ytht) @ rotz(ztht)
    for k in a:
        newarr[k] = operation(newarr[k], rottot)
    return newarr
    
    for i in oldarr:
        arr = rotx(xtht) @ roty(ytht) @ rotz(ztht) @ i[:,np.newaxis]
        arr = arr[:,0]
        newarr = np.vstack((newarr, arr))
    newarr = newarr[1:]
    return newarr

# Draws the shape of the arrays in the various forms of rotations
def rotthrshape(Pthr, Cpthr, xtht=2*np.pi, ytht=2*np.pi, ztht=2*np.pi):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    Pthscales = np.zeros(6)
    Pthfirst = Pthr[:-1]
    Pthlast = Pthr[1:]
    Pthfull = np.hstack((Pthfirst, Cpthr, Pthlast))
    for i in Pthfull:
        Pthpart = rotthr(i.reshape(-1,3), xtht, ytht, ztht)
        ax.plot(Pthpart[:,0],Pthpart[:,1],Pthpart[:,2],'b')
        valtab = np.array([np.min(Pthpart[:,0]), np.max(Pthpart[:,0]), 
                           np.min(Pthpart[:,1]), np.max(Pthpart[:,1]), 
                           np.min(Pthpart[:,2]), np.max(Pthpart[:,2])])
        Pthscales = np.vstack((Pthscales, valtab))
    Pthscales = Pthscales[1:]
    xi, xa = Pthscales[:,0].min(), Pthscales[:,1].max()
    yi, ya = Pthscales[:,2].min(), Pthscales[:,3].max()
    zi, za = Pthscales[:,4].min(), Pthscales[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    
    plt.show()
    
# Multiple rotations, except it's plotted on separate graphs each time
def mulrotthrshapes(Pthr, Cpthr, xtht=2*np.pi, xn=1, ytht=2*np.pi, yn=1, 
                    ztht=2*np.pi, zn=1):
    aa = np.arange(xn)+1
    bb = np.arange(yn)+1
    cc = np.arange(zn)+1
    for i in aa:
        for j in bb:
            for k in cc:
                rotthrshape(Pthr, Cpthr, xtht*i, ytht*j, ztht*k)
                
# The final "Magnum opus" of rotations if you will. Multiple rotations, but
# pn one graph!
def HighCastellan(Pthr, Cpthr, xtht=2*np.pi, xn=1, ytht=2*np.pi, yn=1, 
                  ztht=2*np.pi, zn=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    aa = np.arange(xn)+1
    bb = np.arange(yn)+1
    cc = np.arange(zn)+1
    Pthscales = np.zeros(6)
    Pthfirst = Pthr[:-1]
    Pthlast = Pthr[1:]
    Pthfull = np.hstack((Pthfirst, Cpthr, Pthlast))
    for i in aa:
        for j in bb:
            for k in cc:
                for l in Pthfull:
                    Pthpart = rotthr(l.reshape(-1,3), xtht*i, ytht*j, ztht*k)
                    ax.plot(Pthpart[:,0],Pthpart[:,1],Pthpart[:,2],'b')
                    valtab = np.array([np.min(Pthpart[:,0]), 
                                       np.max(Pthpart[:,0]), 
                                       np.min(Pthpart[:,1]), 
                                       np.max(Pthpart[:,1]), 
                                       np.min(Pthpart[:,2]), 
                                       np.max(Pthpart[:,2])])
                    Pthscales = np.vstack((Pthscales, valtab))
    Pthscales = Pthscales[1:]
    xi, xa = Pthscales[:,0].min(), Pthscales[:,1].max()
    yi, ya = Pthscales[:,2].min(), Pthscales[:,3].max()
    zi, za = Pthscales[:,4].min(), Pthscales[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    
    plt.show()
