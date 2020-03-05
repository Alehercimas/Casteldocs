# Full version of the Bezier curves in 2D and their rotations

import numpy as np
import matplotlib.pyplot as plt

def rot(coor, th):
    rott = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    coor = coor[:, np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def castestrt(s, tht):
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
        q[k] = rot(q[k],tht)
    plt.axis('equal')
    plt.plot(q[:,0],q[:,1],'black')
    return

def castelsimprot(P, Cp, tht):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    for i in Pfull:
        castestrt(i.reshape(-1,2), tht)
    return

# The "automatic" version that computes (n-1) rotations
def manyrots(P, Cp, n):
    plt.figure(figsize=(12,12))
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        castelsimprot(P, Cp, i)
    return

# The "manual" version deciding the angle and number of rotations yourself
def manualrots(P, Cp, tht, n=1):
    nis = np.arange(n) + 1
    for i in nis:
        castelsimprot(P, Cp, tht*i)
    return
