# Practice file for another Bezier Curve, this time a Cubic with four control points.

import numpy as np
import matplotlib.pyplot as plt

# More Coordimates this time
P0 = np.array([1,5])
P1 = np.array([-5,16])
P2 = np.array([10,4])
P3 = np.array([15,9])

# "Slightly" different parameter values this time
t = np.linspace(0,1,101) # BTW linspace 101 makes the curve smoother

# Entering the placeholder coordinate matrix again
p = np.array([0,0])

# The python loop for a Cubic Bezier curve, the code line is long hence it's
# split using the "\" backspace sort of thing.
for i in t:
    p = np.append(p,(P0*((1-i)**3) + P1*(3*i*((1-i)**2)) + \
                     P2*(3*(i**2)*(1-i)) + P3*(i**3))).reshape(-1,2)
  # after appending, the array is reshaped to always be n*2 hence the "-1"  

# Removing the placeholder coordinates as before
p = p[1:]

# Plotting the curve
plt.plot(p[:,0],p[:,1],'r')
