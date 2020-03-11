# The first set of functions for generating a Bezier surface patch using a 
# two dimensional (and heavily edited by moi!) variant of the de Casteljau Algorithm

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

def surfcast(Psur, mpar, npar):# arbitrary parameters m and n
    Psur2 = Psur.copy() # Need to do this so the system doesn't go haywire
    Psur2 = Psur2.astype(float)
    aaa, bbb = Psur2.shape
    bbb = np.arange(aaa-1, 0, -1) # use up the bbb array and set up count matrix
    aaa = np.arange(aaa)
    aaa = aaa[:-1]
    for i in bbb:
        for j in aaa[:i]:
            Psur2[j] = ((1-mpar)*Psur2[j]) + (mpar*Psur2[j+1]) # Summing rows
    Psur2 = Psur2[0].reshape(-1,3) # now reshape this for another loop
    aaa, bbb = Psur2.shape
    bbb = np.arange(aaa-1, 0, -1)
    aaa = np.arange(aaa)
    aaa = aaa[:-1]
    for k in bbb:
        for l in aaa[:k]:
            Psur2[l] = ((1-npar)*Psur2[l]) + (npar*Psur2[l+1])
    Psur2 = Psur2[0]
    return Psur2
       
def surfbez(Psur):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    count = np.arange(11) # for easier "python" like counting
    mpar = np.linspace(0,1,11)
    npar = np.linspace(0,1,11)
    allcoors = np.array([0,0,0])
    for m in count:
        for n in count:
            coors = surfcast(Psur, mpar[m], npar[n])
            allcoors = np.append(allcoors, coors).reshape(-1,3)
    allcoors = allcoors[1:]# remove the zero array at the beginning
    X = allcoors[:,0].reshape(11,11)
    Y = allcoors[:,1].reshape(11,11)
    Z = allcoors[:,2].reshape(11,11)# 11 times 11 parameters in each case
    xi, xa = X.min(), X.max()# And the "proportional" reshaping begins
    yi, ya = Y.min(), Y.max()
    zi, za = Z.min(), Z.max()
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    ax.plot_surface(X, Y, Z, cmap=cm.viridis)
    plt.show()
    return
