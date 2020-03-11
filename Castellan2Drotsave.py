# Create many rotations and save them for later gif creation

import numpy as np
import matplotlib.pyplot as plt
from os import path
# for some n that will be repeated
# pyath = "C:/Users/kamgh/Pictures/Castelpics/Latestsaves"
# plt.savefig(path.join(pyath, "filename_{0}.png".format(n)))

def rot(coor, th):
    rott = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    coor = coor[:, np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def doubrot(coor, th1, th2):
    rot1 = np.array([[np.cos(th1), -np.sin(th1)], [np.sin(th1), np.cos(th1)]])
    rot2 = np.array([[np.cos(th2), -np.sin(th2)], [np.sin(th2), np.cos(th2)]])
    coor = coor[:, np.newaxis]
    coor = rot1 @ coor
    coor = rot2 @ coor
    coor = coor[:,0]
    return coor

def arrify(arry):
    tz = arry[1:-1].copy()#make a duplicate of the reverses
    tz = tz[::-1]
    arry = np.append(arry, tz)
    indz = np.arange(arry.size)
    arry = np.vstack((indz, arry))
    return arry.T

def Castel(s):
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
    plt.axis('equal')
    plt.plot(q[:,0],q[:,1],'black')
    return q

def Castelrot(s, tht):
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
    plt.axis('off')
    plt.plot(q[:,0],q[:,1],'black')
    return q

def Casteldoubrot(s, tht1, tht2):
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
        q[k] = doubrot(q[k], tht1, tht2)
    plt.axis('equal')
    plt.axis('off')
    plt.plot(q[:,0],q[:,1],'black')
    return q

def Bezier(P, Cp):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    Qmany = np.array([0,0])
    for i in Pfull:
        Bezi = Castel(i.reshape(-1,2))
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'black')
    return

def Bezierot(P, Cp, tht):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    Qmany = np.array([0,0])
    for i in Pfull:
        Bezi = Castelrot(i.reshape(-1,2), tht)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'black')
    return Qmany

def Bezierotw(Q, Cq, tht):
    Qfirst = Q[:-1]
    Qlast = Q[1:]
    Qfull = np.hstack((Qfirst, Cq, Qlast))
    Qmany = np.array([0,0])
    for i in Qfull:
        Bezi = Castelrot(i.reshape(-1,2), tht)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'white')
    return Qmany

def Bezierotr(R, Cr, tht):
    Rfirst = R[:-1]
    Rlast = R[1:]
    Rfull = np.hstack((Rfirst, Cr, Rlast))
    Qmany = np.array([0,0])
    for i in Rfull:
        Bezi = Castelrot(i.reshape(-1,2), tht)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'red')
    return Qmany

def Manyrotsuave(P, Cp, n, co=0, cu=0):# Uneven rotations
    plt.figure(figsize=(10, 10))
    pis = np.linspace(0, np.pi*2, n)
    ss, sz = Cp.shape
    #pyath = "C:/Users/kamgh/Pictures/Castelpics/Latestsaves"
    for mm in pis:
        Ph, Cph = P.copy(), Cp.copy()
        Ph[:, 0], Ph[:, 1] =  Ph[:, 0] + co, Ph[:, 1] + cu
        Cph[:, 0:sz:2], Cph[:, 1:sz:2] = Cph[:, 0:sz:2]+co, Cph[:, 1:sz:2]+cu
        Bezierot(Ph, Cph, mm)
    #plt.savefig(path.join(pyath, "Zanynew_{0}.png".format(i)))
    return

def Manyrotsave(P, Cp, n, i=0, co=0):
    plt.figure(figsize=(10, 10))
    pis = np.linspace(0, np.pi*2, n)
    pyath = "C:/Users/kamgh/Pictures/Castelpics/Latestsaves"
    for mm in pis:
        Bezierot(P+co, Cp+co, mm)
    plt.savefig(path.join(pyath, "threerotoftwo_{0}.png".format(i)))
    return
#Now for i in arrify(arry): print i[0] for index and i[1] for the length
    
def Manydoubrotsave(P, Cp, R, Cr, n, i=0, cop=0, cor=0):
    plt.figure(figsize=(12, 12))
    pis = np.linspace(0, np.pi*2, n)
    pyath = "C:/Users/kamgh/Pictures/Castelpics/Latestsaves"
    for mm in pis:
        Bezierotw(P+cop, Cp+cop, mm)
        Bezierotr(R+cor, Cr+cor, mm)
    plt.savefig(path.join(pyath, "Doublerots_{0}.png".format(i)))
    return
