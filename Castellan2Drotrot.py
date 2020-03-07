# A version of a the simpler rotation of a set of Bezier curves
# but it's a "rotation of rotations"

import numpy as np
import matplotlib.pyplot as plt

def rotrot(coor, th1, th2):
    rot1 = np.array([[np.cos(th1), -np.sin(th1)], [np.sin(th1), np.cos(th1)]])
    rot2 = np.array([[np.cos(th2), -np.sin(th2)], [np.sin(th2), np.cos(th2)]])
    coor = coor[:, np.newaxis]
    coor = rot1 @ coor
    coor = rot2 @ coor
    coor = coor[:,0]
    return coor

def castestrtrt(s, tht1, tht2):
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
        q[k] = rotrot(q[k], tht1, tht2)
    plt.axis('equal')
    plt.plot(q[:,0], q[:,1], 'black')
    return

def bezrotrot(P, Cp, tht1, tht2):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    for i in Pfull:
        castestrtrt(i.reshape(-1,2), tht1, tht2)
    return
