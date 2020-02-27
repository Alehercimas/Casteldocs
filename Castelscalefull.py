# All the scaling functions in one place with a function for multiple scales

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def scale3m(coor, x, y, z):
    scal = np.array([[x, 0, 0], [0, y, 0], [0, 0, z]])
    coor = coor[:,np.newaxis]
    coor = scal @ coor
    coor = coor[:,0]
    return coor

def scale3m2(s, xx, yy, zz): 
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
        q[k] = scale3m(q[k], xx, yy, zz)
    return q

# Multiple scales/scalings    
def scale3m4(Pthr, Cpthr, xx, yy, zz, xnum=1, ynum=1, znum=1):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    xnums, ynums, znums = np.arange(xnum), np.arange(ynum), np.arange(znum)
    xnums, ynums, znums = xnums + 1, ynums + 1, znums + 1# removing the zero
    Pthfirst = Pthr[:-1]
    Pthlast = Pthr[1:]
    Pscales = np.zeros(6)
    Pthfull = np.hstack((Pthfirst, Cpthr, Pthlast))
    for i in xnums:
        for j in ynums:
            for k in znums:
                for l in Pthfull:
                    m = scale3m2(l.reshape(-1,3), xx*i, yy*j, zz*k)
                    ax.plot(m[:,0],m[:,1],m[:,2],'b')
                    valtab = np.array([np.min(m[:,0]), np.max(m[:,0]), 
                                       np.min(m[:,1]), np.max(m[:,1]), 
                                       np.min(m[:,2]), np.max(m[:,2])])
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
