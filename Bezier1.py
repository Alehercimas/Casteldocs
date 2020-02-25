import numpy as np
import matplotlib.pyplot as plt

# Example Coordimates
P0 = np.array([-5,-4])
P1 = np.array([-1,3])
P2 = np.array([3,-3])

# The sample parameter t from 0 to 1
t = np.linspace(0,1,11)

# generic placeholder coordinate matrix 
p = np.array([0,0])

#A python loop that adds a coordinate part to p at each parametric value
for i in t:
    p = np.append(p,(P0*((1-i)**2) + P1*(2*i*(1-i)) + P2*(i**2))).reshape(-1,2)
  # after appending, the array is reshaped to always be n*2 hence the "-1"  

# The now unneeded first placeholder row is removed
p = p[1:]

# And now you plot the curve!
plt.plot(p[:,0],p[:,1],'r')
