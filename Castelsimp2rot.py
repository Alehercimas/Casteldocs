# The edited "intermediate" function for the casteljau algorithm with rotation (Castest3rot.py)

import numpy as np
import matplotlib.pyplot as plt

def castelsimprot(P, Cp, tht):
    
    Pfirst = P[:-1] # Create the "P0" control points from P
    Plast = P[1:] # Create the "PN" control points from P
    Pfull = np.hstack((Pfirst, Cp, Plast)) # Combine the control points
    for i in Pfull:
        castestrt(i.reshape(-1,2), tht) # Works out a Curve for each row
