# A function to plot as many surfaces as you wish
# Bauble because each surface patch can be rotated in xyz degrees

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
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

def Grandbauble(xtrn, ytrn, ztrn, xturns=1, yturns=1, zturns=1, 
                xslt=0, yslt=0, zslt=0, *Psur):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    maxminsofar = np.zeros(6)
    for j in enumerate(Psur):
        allcoors = np.array([0,0,0])
        graphlims = np.zeros(6)
        turnstilex = np.arange(xturns[j[0]])+1
        turnstiley = np.arange(yturns[j[0]])+1
        turnstilez = np.arange(zturns[j[0]])+1
        for k in turnstilex:
            for l in turnstiley:
                for m in turnstilez:
                    allcoors = np.array([0,0,0])
                    for n in count:
                        for o in count:
                            coors = surfcast(j[1], mpar[n], npar[o])
                            coors = operation(coors, rotx(xtrn[j[0]]*k))
                            coors = operation(coors, roty(ytrn[j[0]]*l))
                            coors = operation(coors, rotz(ztrn[j[0]]*m))
                            allcoors = np.append(allcoors, coors).reshape(-1,3)
                    allcoors = allcoors[1:]
                    X = allcoors[:,0].reshape(11,11)
                    Y = allcoors[:,1].reshape(11,11)
                    Z = allcoors[:,2].reshape(11,11)
                    X, Y, Z = X + xslt[j[0]], Y + yslt[j[0]], Z + zslt[j[0]]
                    ax.plot_surface(X + xslt[j[0]], Y + yslt[j[0]], 
                                    Z + zslt[j[0]], cmap=cm.viridis)
                    limptemps = np.array([X.min(), X.max(), Y.min(), Y.max(), 
                                          Z.min(), Z.max()])
                    graphlims = np.append(graphlims, limptemps).reshape(-1,6)
        graphlims = graphlims[1:]
        xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
        yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
        zi, za = graphlims[:,4].min(), graphlims[:,5].max()
        maxmin = np.array([xi, xa, yi, ya, zi, za])# Keep the values remembered
        maxminsofar = np.vstack((maxminsofar, maxmin))
    maxminsofar = maxminsofar[1:]
    xiprp, xaprp = maxminsofar[:,0].min(), maxminsofar[:,1].max()
    yiprp, yaprp = maxminsofar[:,2].min(), maxminsofar[:,3].max()
    ziprp, zaprp = maxminsofar[:,4].min(), maxminsofar[:,5].max()
    centre = np.array([xiprp + xaprp, yiprp + yaprp, ziprp + zaprp])/2
    line = max((xaprp - xiprp),(yaprp - yiprp),(zaprp - ziprp))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.axis('off')
    plt.show()
    return
