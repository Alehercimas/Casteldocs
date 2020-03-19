# Just a handful of brief functions to convert my specific coordinates from 2D to 3D with 
# one of the new x, y or z coordinates being zero

def thrdifyx(P, Cp, Plot=False):
    P3 = np.vstack(((np.zeros(P.shape)[:,0]), P.T)).T
    aa, bb, cc = np.hsplit(Cp,3)
    aa = np.vstack(((np.zeros(aa.shape)[:,0]), aa.T)).T
    bb = np.vstack(((np.zeros(bb.shape)[:,0]), bb.T)).T
    cc = np.vstack(((np.zeros(cc.shape)[:,0]), cc.T)).T
    Cp3 = np.hstack((aa,bb,cc))
    del(aa, bb, cc)
    if Plot is True:
        Bezi3r(P3, Cp3)
    return P3, Cp3

def thrdifyy(P, Cp, Plot=False):
    pa, pb = np.hsplit(P,2)
    P3 = np.hstack((pa, np.zeros(pa.shape), pb))
    aa, bb, cc = np.hsplit(Cp,3)
    Cp3 = np.vstack((aa,bb,cc))
    aa, bb = np.hsplit(Cp3,2)# reusing values
    Cp3 = np.hstack((aa, np.zeros(aa.shape), bb))
    aa, bb, cc = np.vsplit(Cp3, 3)
    Cp3 = np.hstack((aa,bb,cc))
    if Plot is True:
        Bezi3r(P3, Cp3)
    return P3, Cp3

def thrdifyz(P, Cp, Plot=False):# Get a 3D coordinate with z-axis =0
    P3 = np.vstack((P.T, (np.zeros(P.shape)[:,0]))).T
    aa, bb, cc = np.hsplit(Cp,3)
    aa = np.vstack((aa.T, (np.zeros(aa.shape)[:,0]))).T
    bb = np.vstack((bb.T, (np.zeros(bb.shape)[:,0]))).T
    cc = np.vstack((cc.T, (np.zeros(cc.shape)[:,0]))).T
    Cp3 = np.hstack((aa,bb,cc))
    del(aa, bb, cc)
    if Plot is True:
        Bezi3r(P3, Cp3)
    return P3, Cp3
