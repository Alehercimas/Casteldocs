# A group of functions that ultimately inverts a 2D set of bezier curves
# around a circle of arbitrary radius and centre.

import numpy as np
import matplotlib.pyplot as plt

def inversi(coor, xzr=0, yzr=0, radi=1):
    zerocoor = np.complex(xzr, yzr)
    coormplex = np.complex(coor[0], coor[1])
    coormplex = np.conj(coormplex-zerocoor)
    coormplex = ((radi**2)/(coormplex)) + zerocoor
    coor = np.array([coormplex.real, coormplex.imag])
    return coor

def castestinv(s, xzr=0, yzr=0, radi=1):
    pp = np.hstack((s[:-1], s[1:]))
    a, b = np.shape(s)
    c = np.arange(a - b)
    t = np.linspace(0,1,11)
    p = np.array([0,0])
    q = np.array([0,0])
    Theta = np.linspace(0,np.pi*2, 51)
    cosinus = np.array([])
    sinus = np.array([])
    for i in Theta:
        cosinus = np.append(cosinus,(7*np.cos(i)-1))
        sinus = np.append(sinus, (7*np.sin(i)-2))
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-2]) + (h*j[2:]))).reshape(-1,2)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0])
        q = np.append(q, (((1-h)*pp[:,:-2]) + (h*pp[:,2:]))).reshape(-1,2)
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    plt.plot(q[:,0],q[:,1],'b')
    a, b = np.shape(q)
    a = np.arange(a)
    for k in a:
        q[k] = inversi(q[k], xzr, yzr, radi)
    plt.axis('equal')
    plt.plot(cosinus, sinus)
    plt.plot(q[:,0],q[:,1],'b')
    return

def castelsinv(P, Cp, xzr=0, yzr=0, radi=1):
    
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    for i in Pfull:
        castestinv(i.reshape(-1,2), xzr, yzr, radi)
    return
