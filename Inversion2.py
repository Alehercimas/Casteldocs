# Varying functions that that both invert and rotate a set of Bezier curves
# around a circle of arbitrary radius and centre.

import numpy as np
import matplotlib.pyplot as plt

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

def castrotinv(s, tht, xzr=0, yzr=0, radi=1):
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
    #p = q.copy()
    a, b = np.shape(q)
    a = np.arange(a)
    for k in a:
        q[k] = rot(q[k],tht)
        #p[k] = rot(p[k],tht)
        q[k] = inversi(q[k], xzr, yzr, radi)
    #plt.xlim(-20, 20)
    #plt.ylim(-15, 15)
    plt.axis('equal')
    #plt.plot(p[:,0],p[:,1],'b')
    plt.plot(q[:,0],q[:,1],'b')
    return

def bezrotinv(P, Cp, tht, xzr=0, yzr=0, radi=1):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    for i in Pfull:
        castrotinv(i.reshape(-1,2), tht, xzr, yzr, radi)
    return

def manyrotinvs(P, Cp, n, xzr=0, yzr=0, radi=1):
    plt.figure(figsize=(12,9))
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        bezrotinv(P, Cp, i, xzr, yzr, radi)
    return

def manualrotinvs(P, Cp, tht, n=1, xzr=0, yzr=0, radi=1):
    nis = np.arange(n) + 1
    for i in nis:
        bezrotinv(P, Cp, tht*i, xzr, yzr, radi)
    return
