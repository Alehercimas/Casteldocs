# A function for taking a set of Bezier curves (Po and Cpo) "pushing" them to the third dimension
# and translating them by (xcor, ycor, zcor)

def Bezi3rd(Po, Cpo, Axis, xcor=0, ycor=0, zcor=0):
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca(projection='3d')
    if Axis == 'x':
        Points, Controlpoints = thrdifyx(Po, Cpo)
    elif Axis == 'y':
        Points, Controlpoints = thrdifyy(Po, Cpo)
    elif Axis == 'z':
        Points, Controlpoints = thrdifyz(Po, Cpo)
    aa, bb = Controlpoints.shape
    Doints = Points.copy()
    Dontrol = Controlpoints.copy()
    Doints[:, 0] = Doints[:, 0] + xcor
    Doints[:, 1] = Doints[:, 1] + ycor
    Doints[:, 2] = Doints[:, 2] + zcor
    Dontrol[:, 0:bb:3] = Dontrol[:, 0:bb:3] + xcor
    Dontrol[:, 1:bb:3] = Dontrol[:, 1:bb:3] + ycor
    Dontrol[:, 2:bb:3] = Dontrol[:, 2:bb:3] + zcor
    Pscales = np.zeros(6)
    Pointfirst = Doints[:-1]
    Pointlast = Doints[1:]
    Pointfull = np.hstack((Pointfirst, Dontrol, Pointlast))
    Allcoors = np.array([0,0,0])
    for j in Pointfull:
        #ax.plot(j.reshape(-1,3)[:,0], j.reshape(-1,3)[:,1], 
                #j.reshape(-1,3)[:,2], 'red')# control polygon visible
        k = castest3d(j.reshape(-1,3))
        ax.plot(k[:,0],k[:,1],k[:,2], linewidth=5, color='black')
        valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                           np.min(k[:,1]), np.max(k[:,1]), 
                           np.min(k[:,2]), np.max(k[:,2])])
        Pscales = np.vstack((Pscales, valtab))
        Allcoors = np.vstack((Allcoors, k))
    Allcoors = Allcoors[1:]
    Allx, Ally, Allz = Allcoors[:,0], Allcoors[:,1], Allcoors[:,2]
    Filledpart = [list(zip(Allx, Ally, Allz))]
    ax.add_collection3d(Poly3DCollection(Filledpart, facecolors='w'))
    Pscales = Pscales[1:]
    xi = Pscales[:,0].min()
    xa = Pscales[:,1].max()
    yi = Pscales[:,2].min()
    ya = Pscales[:,3].max()
    zi = Pscales[:,4].min()
    za = Pscales[:,5].max()
    del Pscales
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))/2
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    #plt.axis('off')
    plt.show()
    return
