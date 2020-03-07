# A sort of "Pseudo-2D" plot
# Multiple rotations and inversions, arranged in 3D space in successive
# "slices" along the positive z axis. The circles of inversion can either
# increase or decrease

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def rot(coor, th):
    rott = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    coor = coor[:, np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def inversi(coor, xzr=0, yzr=0, radi=1):
    zerocoor = np.complex(xzr, yzr)
    coormplex = np.complex(coor[0], coor[1])
    coormplex = np.conj(coormplex-zerocoor)
    coormplex = ((radi**2)/(coormplex)) + zerocoor
    coor = np.array([coormplex.real, coormplex.imag])
    return coor

def castrotinvth(s, tht, xzr=0, yzr=0, radi=1, zpos=0):
    pp = np.hstack((s[:-1], s[1:]))
    a, b = np.shape(s)
    c = np.arange(a - b)
    t = np.linspace(0,1,11)
    p = np.array([0,0])
    q = np.array([0,0])
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-2]) + (h*j[2:]))).reshape(-1,2)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0])
        q = np.append(q, (((1-h)*pp[:,:-2]) + (h*pp[:,2:]))).reshape(-1,2)
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    a, b = np.shape(q)
    qzer = np.zeros(a).reshape(-1,1)
    qzer = qzer + zpos
    a = np.arange(a)
    for k in a:
        q[k] = rot(q[k],tht)
        q[k] = inversi(q[k], xzr, yzr, radi)
    q = np.hstack((q, qzer))
    return q

def bezrotinvthr(P, Cp, tht, xzr=0, yzr=0, radi=1, zpos=0):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    bigarr = np.zeros(3)
    for i in Pfull:
        towerslice = castrotinvth(i.reshape(-1,2), tht, xzr, yzr, radi, zpos)
        bigarr = np.vstack((bigarr, towerslice))
    bigarr = bigarr[1:]
    return bigarr

def crazyflower(P, Cp, tht, n=1, xzr=0, yzr=0, radi=1, 
                   nofsteps=0, stepln=0, rever=False):
    fig = plt.figure(figsize=(12,9))
    ax = fig.gca(projection='3d')
    nis = np.arange(n)
    ztower = np.arange(nofsteps + 1)
    zradius = np.linspace(radi, (radi + (nofsteps * stepln)), (nofsteps+1))
    if rever == True:
        zradius = zradius[::-1]
    for i in ztower:
        for j in nis:
            bigger = bezrotinvthr(P, Cp, tht*j, xzr, yzr, zradius[i], i)
            ax.plot(bigger[:,0], bigger[:,1], bigger[:,2],'b')
    plt.show()
    return
