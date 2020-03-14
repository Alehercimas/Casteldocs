# Casteljau/Bezier cleanup with multiple axes of rotation, shown further below

import numpy as np
import matplotlib.pyplot as plt

def rotplus(coor, th, xcr=0, ycr=0):
    rott = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    coor = coor[:, np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    coor[0], coor[1] = coor[0] + xcr, coor[1] + ycr# send it back
    return coor

def doubrot(coor, th1, th2):
    rot1 = np.array([[np.cos(th1), -np.sin(th1)], [np.sin(th1), np.cos(th1)]])
    rot2 = np.array([[np.cos(th2), -np.sin(th2)], [np.sin(th2), np.cos(th2)]])
    coor = coor[:, np.newaxis]
    coor = rot1 @ coor
    coor = rot2 @ coor
    coor = coor[:,0]
    return coor

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

def Castelrot(s, tht, xcr=0, ycr=0):
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
        q[k] = rotplus(q[k], tht, xcr, ycr)
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
        #plt.plot(i.reshape(-1,2)[:,0], i.reshape(-1,2)[:,1],'red')
        Bezi = Castel(i.reshape(-1,2))
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'black')
    return #Qmany

def manybezs(*args):
    plt.figure(figsize=(10, 10))
    args = Manyrots()
    plt.show()
    return

def Bezierot(P, Cp, tht, xcr=0, ycr=0):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    Qmany = np.array([0,0])
    for i in Pfull:
        Bezi = Castelrot(i.reshape(-1,2), tht, xcr, ycr)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'black')
    return #Qmany

def Bezierotw(Q, Cq, tht, xcr=0, ycr=0):
    Qfirst = Q[:-1]
    Qlast = Q[1:]
    Qfull = np.hstack((Qfirst, Cq, Qlast))
    Qmany = np.array([0,0])
    for i in Qfull:
        Bezi = Castelrot(i.reshape(-1,2), tht, xcr, ycr)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'white')
    return Qmany

def Bezierotr(R, Cr, tht, xcr=0, ycr=0):
    Rfirst = R[:-1]
    Rlast = R[1:]
    Rfull = np.hstack((Rfirst, Cr, Rlast))
    Qmany = np.array([0,0])
    for i in Rfull:
        Bezi = Castelrot(i.reshape(-1,2), tht, xcr, ycr)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'red')
    return Qmany

def Manyrots(P, Cp, n, cox=0, coy=0, xcr=0, ycr=0):
    #plt.figure(figsize=(10, 10))
    pis = np.linspace(0, np.pi*2, n)
    a, b = Cp.shape
    Peec, Cpeec = P.copy(), Cp.copy()
    Peec[:,0], Peec[:,1] = Peec[:,0] + cox, Peec[:,1] + coy
    Cpeec[:,0:b:2] = Cpeec[:,0:b:2] + cox
    Cpeec[:,1:b:2] = Cpeec[:,1:b:2] + coy
    for i in pis:
        Bezierot(Peec, Cpeec, i, xcr, ycr)
    return

def Manymanyrots(P, Cp, n, cox, coy, xcr, ycr):
    plt.figure(figsize=(10, 10))
    Pfft = np.arange(np.size(n))
    for a in Pfft:
        Manyrots(P[a], Cp[a], n[a], cox[a], coy[a], xcr[a], ycr[a])
    plt.show()
    return

def Manydoubrots(P, Cp, R, Cr, n, xcr=0, ycr=0, copx=0, copy=0, 
                 corx=0, cory=0):
    #plt.figure(figsize=(10, 10))
    pis = np.linspace(0, np.pi*2, n)
    a, b = Cp.shape
    c, d = Cr.shape
    Peec, Cpeec, Reec, Creec = P.copy(), Cp.copy(), R.copy(), Cr.copy()
    Peec[:,0], Reec[:,0] = Peec[:,0] + copx, Reec[:,0] + corx
    Peec[:,1], Reec[:,1] = Peec[:,1] + copy, Reec[:,1] + cory
    Cpeec[:,0:b:2] = Cpeec[:,0:b:2] + copx
    Cpeec[:,1:b:2] = Cpeec[:,1:b:2] + copy
    Creec[:,0:b:2] = Creec[:,0:b:2] + corx
    Creec[:,1:b:2] = Creec[:,1:b:2] + cory
    for i in pis:
        Bezierot(Peec, Cpeec, i, xcr, ycr)
        Bezierot(Reec, Creec, i, xcr, ycr)
    return

def Manymanydoubrots(P, Cp, R, Cr, n, xcr, ycr):
    plt.figure(figsize=(10, 10))
    Pfft = np.arange(np.size(n))
    for a in Pfft:
        Manydoubrots(P[a], Cp[a], R[a], Cr[a], n[a], xcr[a], ycr[a])
    plt.show()
    return
