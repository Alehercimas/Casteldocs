# The first proper function using the "Casteljau" variant to plot a curve for any input
# The input s is any (n * 2) sized matrix.The first and second column corresponds to the x and y coordinates respectively

import numpy as np
import matplotlib.pyplot as plt

def castest(s):
    # Set up a new array pp that's "python friendly" for the "FOR" loops
    pp = np.hstack((s[:-1], s[1:])) 
    
    a, b = np.shape(s)
    # really it should be (a - 2) but I wanted to use all variables 
    c = np.arange(a - b)
    # Parameters t from 0 to 1 as always
    t = np.linspace(0,1,11) 
    # Two placeholder arrays for two loops
    p = np.array([0,0])
    q = np.array([0,0])
    # Here's where the set up takes some editing from the original algorithm
    for h in t:
        for i in c:
            for j in pp:
                p = np.append(p,(((1-h)*j[:-2]) + (h*j[2:]))).reshape(-1,2)
            pp = np.hstack((p[1:-1], p[2:]))
            p = np.array([0,0])
        q = np.append(q, (((1-h)*pp[:,:-2]) + (h*pp[:,2:]))).reshape(-1,2)
        # Arrays return to normal for the next loop iteration
        pp = np.hstack((s[:-1], s[1:]))
    q = q[1:]# Drop the "0th" row
    plt.axis('equal')# obvious plotting an axis
    plt.plot(q[:,0],q[:,1],'b')
