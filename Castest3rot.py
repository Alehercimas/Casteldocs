# An edited casteljau'esque algorithm incorporating the rotation function

import numpy as np
import matplotlib.pyplot as plt

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
        # Arrays return to normal for the next loop iteration
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]
    #The new bits, each coordinate row is changed to its rotated version
    a, b = np.shape(q) # Reuse the value a for another array, (b is unused)
    a = np.arange(a) # Reduce the value so it fits in the next loop
    for k in a:
        q[k] = rot(q[k],tht) # perform the "rotation" function called rot
    plt.axis('equal')
    plt.plot(q[:,0],q[:,1],'b')
