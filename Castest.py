Example using a "De Casteljau" algorithm like variant to plot a Cubic Bezier curve

import numpy as np
import matplotlib.pyplot as plt

D = np.array([[3,2],[1,5],[5,4],[4,7]])
pp = np.hstack((D[:-1], D[1:]))
a, b = np.shape(D)
c = np.arange(a - b)
t = np.linspace(0,1,101)
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
    pp = np.hstack((D[:-1], D[1:]))
q = q[1:]
print(q)
plt.plot(q[:,0],q[:,1],'r')
