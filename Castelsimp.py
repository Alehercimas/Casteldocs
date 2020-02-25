# An "intermediate" function of sorts, getting coordinate arrays and setting 
# them up for calculation in with the "casteljau" method 

import numpy as np
import matplotlib.pyplot as plt

def castelsimp(P, Cp):
    
    Pfirst = P[:-1] # Create the "P0" control points from P
    Plast = P[1:] # Create the "PN" control points from P
    Pfull = np.hstack((Pfirst, Cp, Plast)) # Combine the control points
    for i in Pfull:
        castest(i.reshape(-1,2)) # Works out a Curve for each row
