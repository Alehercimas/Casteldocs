# Rotate an n*3 array (n lots of (x,y,z) coordinates) by theta (tht) in xdir

import numpy as np

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
        # Arrays return to normal for the next loop iteration
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    a, b = np.shape(q)
    a = np.arange(a)
    for k in a:
        q[k] = rot3x(q[k],tht)
    return q
