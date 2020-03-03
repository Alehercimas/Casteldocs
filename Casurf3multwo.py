# Similar to Casurf2mult.py but you can choose all rotations on one function.
# Defaults to a single unrotated surface.
# Choose whichever is more comfortable to use, Casurf2mult or Casurf3multwo

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

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

def scalem(xx, yy, zz):
    scalem = np.array([[xx, 0, 0], [0, yy, 0], [0, 0, zz]])
    return scalem

def operation(coor, trn):
    rott = trn
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def surfcast(Psur, mpar, npar):
    Psur2 = Psur.copy()
    Psur2 = Psur2.astype(float)
    aaa, bbb = Psur2.shape
    bbb = np.arange(aaa-1, 0, -1)
    aaa = np.arange(aaa)
    aaa = aaa[:-1]
    for i in bbb:
        for j in aaa[:i]:
            Psur2[j] = ((1-mpar)*Psur2[j]) + (mpar*Psur2[j+1])
    Psur2 = Psur2[0].reshape(-1,3)
    aaa, bbb = Psur2.shape
    bbb = np.arange(aaa-1, 0, -1)
    aaa = np.arange(aaa)
    aaa = aaa[:-1]
    for k in bbb:
        for l in aaa[:k]:
            Psur2[l] = ((1-npar)*Psur2[l]) + (npar*Psur2[l+1])
    Psur2 = Psur2[0]
    return Psur2
    
def surfmultwo(Psur, axis, trn, turns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11) # for easier "python" like counting
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstile = np.arange(turns)+1
    for l in turnstile:
        allcoors = np.array([0,0,0])
        for m in count:
            for n in count:
                coors = surfcast(Psur, mpar[m], npar[n])
                if axis == 'x':
                    coors = operation(coors, rotx(trn*l))
                if axis == 'y':
                    coors = operation(coors, roty(trn*l))
                if axis == 'z':
                    coors = operation(coors, rotz(trn*l))
                allcoors = np.append(allcoors, coors).reshape(-1,3)
        allcoors = allcoors[1:]# remove the zero array at the beginning
        X = allcoors[:,0].reshape(11,11)
        Y = allcoors[:,1].reshape(11,11)
        Z = allcoors[:,2].reshape(11,11)# 11 times 11 parameters in each case
        ax.plot_surface(X, Y, Z)
        limptemps = np.array([X.min(), X.max(), Y.min(), 
                              Y.max(), Z.min(), Z.max()])
        graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]# Find the most "extreme" scale out of the scales
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    
    plt.show()
