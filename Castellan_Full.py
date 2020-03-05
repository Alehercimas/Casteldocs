# All functions for the rotations of Bezier curves in 3D space in one place
# With an optional function depicting all three

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def rot3x(coor, th):
    rott = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], 
                     [0, np.sin(th), np.cos(th)]])
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def rot3y(coor, th):
    rott = np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], 
                      [-np.sin(th), 0, np.cos(th)]])
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def rot3z(coor, th):
    rott = np.array([[np.cos(th), -np.sin(th), 0], 
                      [np.sin(th), np.cos(th), 0], [0, 0, 1]])
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def castestrot3x(s, tht):
    pp = np.hstack((s[:-1], s[1:]))
    a, b = np.shape(s)
    c = np.arange(a - 2)
    t = np.linspace(0,1,11)
    p = np.array([0,0,0])
    q = np.array([0,0,0])
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-3]) + (h*j[3:]))).reshape(-1,3)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0,0])
        q = np.append(q, (((1-h)*pp[:,:-3]) + (h*pp[:,3:]))).reshape(-1,3)
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    a, b = np.shape(q)
    a = np.arange(a)
    for k in a:
        q[k] = rot3x(q[k],tht)
    return q

def castestrot3y(s, tht):
    pp = np.hstack((s[:-1], s[1:]))
    a, b = np.shape(s)
    c = np.arange(a - 2)
    t = np.linspace(0,1,11)
    p = np.array([0,0,0])
    q = np.array([0,0,0])
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-3]) + (h*j[3:]))).reshape(-1,3)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0,0])
        q = np.append(q, (((1-h)*pp[:,:-3]) + (h*pp[:,3:]))).reshape(-1,3)
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    a, b = np.shape(q)
    a = np.arange(a)
    for k in a:
        q[k] = rot3y(q[k],tht)
    return q

def castestrot3z(s, tht):
    pp = np.hstack((s[:-1], s[1:]))
    a, b = np.shape(s)
    c = np.arange(a - 2)
    t = np.linspace(0,1,11)
    p = np.array([0,0,0])
    q = np.array([0,0,0])
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-3]) + (h*j[3:]))).reshape(-1,3)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0,0])
        q = np.append(q, (((1-h)*pp[:,:-3]) + (h*pp[:,3:]))).reshape(-1,3)
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    a, b = np.shape(q)
    a = np.arange(a)
    for k in a:
        q[k] = rot3z(q[k],tht)
    return q

def Castellan(Points, Controlpoints, Axes, Thetnums=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    Pirange = np.linspace(0,np.pi*2,Thetnums)
    Pscales = np.zeros(6)
    Pointfirst = Points[:-1]
    Pointlast = Points[1:]
    Pointfull = np.hstack((Pointfirst, Controlpoints, Pointlast))
    if Axes == 'x':
        for i in Pirange:
            for j in Pointfull:
                k = castestrot3x(j.reshape(-1,3), i)
                ax.plot(k[:,0],k[:,1],k[:,2],'b')
                valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                   np.min(k[:,1]), np.max(k[:,1]), 
                                   np.min(k[:,2]), np.max(k[:,2])])
                Pscales = np.vstack((Pscales, valtab))
    elif Axes == 'y':
        for i in Pirange:
            for j in Pointfull:
                k = castestrot3y(j.reshape(-1,3), i)
                ax.plot(k[:,0],k[:,1],k[:,2],'b')
                valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                   np.min(k[:,1]), np.max(k[:,1]), 
                                   np.min(k[:,2]), np.max(k[:,2])])
                Pscales = np.vstack((Pscales, valtab))
    elif Axes == 'z':
        for i in Pirange:
            for j in Pointfull:
                k = castestrot3z(j.reshape(-1,3), i)
                ax.plot(k[:,0],k[:,1],k[:,2],'b')
                valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                   np.min(k[:,1]), np.max(k[:,1]), 
                                   np.min(k[:,2]), np.max(k[:,2])])
                Pscales = np.vstack((Pscales, valtab))
    Pscales = Pscales[1:]
    xi = Pscales[:,0].min()
    xa = Pscales[:,1].max()
    yi = Pscales[:,2].min()
    ya = Pscales[:,3].max()
    zi = Pscales[:,4].min()
    za = Pscales[:,5].max()
    del Pscales
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    plt.show()
