# Full version of Bezier curves and their scalings in 2D

import numpy as np
import matplotlib.pyplot as plt

def scal(coor, xx, yy):
    scall = np.array([[xx, 0], [0, yy]])
    coor = coor[:, np.newaxis]
    coor = scall @ coor
    coor = coor[:, 0]
    return coor

def castestsc(s, xx, yy):
    
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
    a = np.arange(a)
    for k in a:
        q[k] = scal(q[k], xx, yy)
    plt.axis('equal')
    plt.plot(q[:,0],q[:,1],'b')
    return

def castelsimpscl(P, Cp, xx, yy):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    for i in Pfull:
        castestsc(i.reshape(-1,2), xx, yy)
    return

def manyscales(P, Cp, xx, yy, m=1, n=1):
    plt.figure(figsize=(9,9))
    mis = np.arange(m) + 1
    nis = np.arange(n) + 1
    for i in mis:
        for j in nis:
            castelsimpscl(P, Cp, xx*i, yy*j)
    return
