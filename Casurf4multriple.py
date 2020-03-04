# And the final batch for rotating in XYZ, XZY, YXZ, YZX, ZXY and ZYX variants

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
    
def surfmultxyz(Psur, xtrn, ytrn, ztrn, xturns=1, yturns=1, zturns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstilex = np.arange(xturns)+1
    turnstiley = np.arange(yturns)+1
    turnstilez = np.arange(zturns)+1
    for k in turnstilex:
        for l in turnstiley:
            for m in turnstilez:
                allcoors = np.array([0,0,0])
                for n in count:
                    for o in count:
                        coors = surfcast(Psur, mpar[n], npar[o])
                        coors = operation(coors, rotx(xtrn*k))
                        coors = operation(coors, roty(ytrn*l))
                        coors = operation(coors, rotz(ztrn*m))
                        allcoors = np.append(allcoors, coors).reshape(-1,3)
                allcoors = allcoors[1:]
                X = allcoors[:,0].reshape(11,11)
                Y = allcoors[:,1].reshape(11,11)
                Z = allcoors[:,2].reshape(11,11)
                ax.plot_surface(X, Y, Z, cmap=cm.viridis)
                limptemps = np.array([X.min(), X.max(), Y.min(), 
                                      Y.max(), Z.min(), Z.max()])
                graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
    return

def surfmultxzy(Psur, xtrn, ztrn, ytrn, xturns=1, zturns=1, yturns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstilex = np.arange(xturns)+1
    turnstilez = np.arange(zturns)+1
    turnstiley = np.arange(yturns)+1
    for k in turnstilex:
        for l in turnstilez:
            for m in turnstiley:
                allcoors = np.array([0,0,0])
                for n in count:
                    for o in count:
                        coors = surfcast(Psur, mpar[n], npar[o])
                        coors = operation(coors, rotx(xtrn*k))
                        coors = operation(coors, rotz(ztrn*l))
                        coors = operation(coors, roty(ytrn*m))
                        allcoors = np.append(allcoors, coors).reshape(-1,3)
                allcoors = allcoors[1:]
                X = allcoors[:,0].reshape(11,11)
                Y = allcoors[:,1].reshape(11,11)
                Z = allcoors[:,2].reshape(11,11)
                ax.plot_surface(X, Y, Z, cmap=cm.viridis)
                limptemps = np.array([X.min(), X.max(), Y.min(), 
                                      Y.max(), Z.min(), Z.max()])
                graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
    return

def surfmultyxz(Psur, ytrn, xtrn, ztrn, yturns=1, xturns=1, zturns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstiley = np.arange(yturns)+1
    turnstilex = np.arange(xturns)+1
    turnstilez = np.arange(zturns)+1
    for k in turnstiley:
        for l in turnstilex:
            for m in turnstilez:
                allcoors = np.array([0,0,0])
                for n in count:
                    for o in count:
                        coors = surfcast(Psur, mpar[n], npar[o])
                        coors = operation(coors, roty(ytrn*k))
                        coors = operation(coors, rotx(xtrn*l))
                        coors = operation(coors, rotz(ztrn*m))
                        allcoors = np.append(allcoors, coors).reshape(-1,3)
                allcoors = allcoors[1:]
                X = allcoors[:,0].reshape(11,11)
                Y = allcoors[:,1].reshape(11,11)
                Z = allcoors[:,2].reshape(11,11)
                ax.plot_surface(X, Y, Z, cmap=cm.viridis)
                limptemps = np.array([X.min(), X.max(), Y.min(), 
                                      Y.max(), Z.min(), Z.max()])
                graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
    return

def surfmultyzx(Psur, ytrn, ztrn, xtrn, yturns=1, zturns=1, xturns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstiley = np.arange(yturns)+1
    turnstilez = np.arange(zturns)+1
    turnstilex = np.arange(xturns)+1
    for k in turnstiley:
        for l in turnstilez:
            for m in turnstilex:
                allcoors = np.array([0,0,0])
                for n in count:
                    for o in count:
                        coors = surfcast(Psur, mpar[n], npar[o])
                        coors = operation(coors, roty(ytrn*k))
                        coors = operation(coors, rotz(ztrn*l))
                        coors = operation(coors, rotx(xtrn*m))
                        allcoors = np.append(allcoors, coors).reshape(-1,3)
                allcoors = allcoors[1:]
                X = allcoors[:,0].reshape(11,11)
                Y = allcoors[:,1].reshape(11,11)
                Z = allcoors[:,2].reshape(11,11)
                ax.plot_surface(X, Y, Z, cmap=cm.viridis)
                limptemps = np.array([X.min(), X.max(), Y.min(), 
                                      Y.max(), Z.min(), Z.max()])
                graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
    return

def surfmultzxy(Psur, ztrn, xtrn, ytrn, zturns=1, xturns=1, yturns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstilez = np.arange(zturns)+1
    turnstilex = np.arange(xturns)+1
    turnstiley = np.arange(yturns)+1
    for k in turnstilez:
        for l in turnstilex:
            for m in turnstiley:
                allcoors = np.array([0,0,0])
                for n in count:
                    for o in count:
                        coors = surfcast(Psur, mpar[n], npar[o])
                        coors = operation(coors, rotz(ztrn*k))
                        coors = operation(coors, rotx(xtrn*l))
                        coors = operation(coors, roty(ytrn*m))
                        allcoors = np.append(allcoors, coors).reshape(-1,3)
                allcoors = allcoors[1:]
                X = allcoors[:,0].reshape(11,11)
                Y = allcoors[:,1].reshape(11,11)
                Z = allcoors[:,2].reshape(11,11)
                ax.plot_surface(X, Y, Z, cmap=cm.viridis)
                limptemps = np.array([X.min(), X.max(), Y.min(), 
                                      Y.max(), Z.min(), Z.max()])
                graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
    return

def surfmultzyx(Psur, ztrn, ytrn, xtrn, zturns=1, yturns=1, xturns=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11)
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    graphlims = np.zeros(6)
    turnstilez = np.arange(zturns)+1
    turnstiley = np.arange(yturns)+1
    turnstilex = np.arange(xturns)+1
    for k in turnstilez:
        for l in turnstiley:
            for m in turnstilex:
                allcoors = np.array([0,0,0])
                for n in count:
                    for o in count:
                        coors = surfcast(Psur, mpar[n], npar[o])
                        coors = operation(coors, rotz(ztrn*k))
                        coors = operation(coors, roty(ytrn*l))
                        coors = operation(coors, rotx(xtrn*m))
                        allcoors = np.append(allcoors, coors).reshape(-1,3)
                allcoors = allcoors[1:]
                X = allcoors[:,0].reshape(11,11)
                Y = allcoors[:,1].reshape(11,11)
                Z = allcoors[:,2].reshape(11,11)
                ax.plot_surface(X, Y, Z, cmap=cm.viridis)
                limptemps = np.array([X.min(), X.max(), Y.min(), 
                                      Y.max(), Z.min(), Z.max()])
                graphlims = np.append(graphlims, limptemps).reshape(-1,6)
    graphlims = graphlims[1:]
    xi, xa = graphlims[:,0].min(), graphlims[:,1].max()
    yi, ya = graphlims[:,2].min(), graphlims[:,3].max()
    zi, za = graphlims[:,4].min(), graphlims[:,5].max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
    return
