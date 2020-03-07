# Many varied functions in 2D space.
# Mostly Bezier/de Casteljau equations, but they generate
# a filled set of bezier curves, with a feature to rotate up to
# four sets of Bezier curves.

import numpy as np
import matplotlib.pyplot as plt

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
    return Qmany

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

def Beziedoubrot(P, Cp, tht1, tht2):
    Pfirst = P[:-1]
    Plast = P[1:]
    Pfull = np.hstack((Pfirst, Cp, Plast))
    Qmany = np.array([0,0])
    for i in Pfull:
        Bezi = Casteldoubrot(i.reshape(-1,2), tht1, tht2)
        Qmany = np.vstack((Qmany, Bezi))
    Qmany = Qmany[1:]
    plt.fill(Qmany[:,0], Qmany[:,1], 'black')
    return Qmany

def Manyrots(P, Cp, n):
    plt.figure(figsize=(10, 10))
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        Bezierot(P, Cp, i)
    return

def Manydoubrots(P, Cp, R, Cr, n):
    plt.figure(figsize=(12, 12))
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        Bezierot(P, Cp, i)
        Bezierotr(R, Cr, i)
    return

def Manytriprots(P, Cp, Q, Cq, R, Cr, n):
    plt.figure(figsize=(12, 12))
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        Bezierot(P, Cp, i)
        Bezierotr(Q, Cq, i)
        Bezierot(R, Cr, i)
    return

def Manyquadrots(P, Cp, Q, Cq, R, Cr, S, Cs, n):
    plt.figure(figsize=(12, 12))
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        Bezierot(P, Cp, i)
        Bezierotr(Q, Cq, i)
        Bezierot(R, Cr, i)
        Bezierotr(S, Cs, i)
    return

def Manuarots(P, Cp, tht, n=1):
    plt.figure(figsize=(5, 5))
    nis = np.arange(n) + 1
    for i in nis:
        Bezierot(P, Cp, tht*i)
    return

def Manuadoubrots(P, Cp, R, Cr, tht, n=1):
    plt.figure(figsize=(5, 5))
    nis = np.arange(n) + 1
    for i in nis:
        Bezierot(P, Cp, tht*i)
        Bezierotr(R, Cr, ((np.pi*2) - tht*(-i)))
    return
