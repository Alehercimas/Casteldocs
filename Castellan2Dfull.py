# Full version of the bezier curves in 2D

import numpy as np
import matplotlib.pyplot as plt

def rot(coor, th):
    rott = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    coor = coor[:, np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def scal(coor, xx, yy):
    scall = np.array([[xx, 0], [0, yy]])
    coor = coor[:, np.newaxis]
    coor = scall @ coor
    coor = coor[:, 0]
    return coor

def castestrtsc(s, tht, xx=1, yy=1):
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
        q[k] = scal(q[k], xx, yy)
    plt.axis('equal')
    plt.plot(q[:,0],q[:,1],'b')
    return

def castelrotscl(P, Cp, tht, xx=1, yy=1):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    for i in Pfull:
        castestrtsc(i.reshape(-1,2), tht, xx, yy)
    return

def rotnscales(P, Cp, tht=np.pi*2, xx=1, yy=1, rtn=1, scn=1):
    rots = np.arange(rtn) + 1
    scls = np.arange(scn) + 1
    for i in rots:
        for j in scls:
            castelrotscl(P, Cp, tht*i, xx*j, yy*j)
    return

# Rotates and enlarges by same amount
def rotnscaleseq(P, Cp, tht=np.pi*2, xx=1, yy=1, seqn=1):
    seqs = np.arange(seqn) + 1
    for i in seqs:
        castelrotscl(P, Cp, tht*i, xx*i, yy*i)
    return
