# A function for taking 

def GrandBezi3r(Po, Cpo, Axis, Theta, Rotxis, Rotn, xcor, ycor, zcor, time=0):
    # plt.style.use('dark_background') # Optional Dark background
    fig = plt.figure(figsize=(12, 12))
    ax = fig.gca(projection='3d')
    Count = np.arange(np.size(Axis))
    GrandControl = np.zeros(6)
    for c in Count:
        if Axis[c] == 'x':
            Points, Controlpoints = thrdifyx(Po[c], Cpo[c])
        elif Axis[c] == 'y':
            Points, Controlpoints = thrdifyy(Po[c], Cpo[c])
        elif Axis[c] == 'z':
            Points, Controlpoints = thrdifyz(Po[c], Cpo[c])
        aa, bb = Controlpoints.shape
        Doints = Points.copy()
        Dontrol = Controlpoints.copy()
        Doints[:, 0] = Doints[:, 0] + xcor[c]
        Doints[:, 1] = Doints[:, 1] + ycor[c]
        Doints[:, 2] = Doints[:, 2] + zcor[c]
        Dontrol[:, 0:bb:3] = Dontrol[:, 0:bb:3] + xcor[c]
        Dontrol[:, 1:bb:3] = Dontrol[:, 1:bb:3] + ycor[c]
        Dontrol[:, 2:bb:3] = Dontrol[:, 2:bb:3] + zcor[c]
        Pirange = np.arange(Rotn[c]) + 1
        Pscales = np.zeros(6)
        Pointfirst = Doints[:-1]
        Pointlast = Doints[1:]
        Pointfull = np.hstack((Pointfirst, Dontrol, Pointlast))
        Allcoors = np.array([0,0,0])
        for i in Pirange:
            for j in Pointfull:
                if Rotxis[c] == 'x':
                    k = castestrot3x(j.reshape(-1,3), Theta[c]*i)
                    ax.plot(k[:,0],k[:,1],k[:,2], linewidth=2, color='black')
                    valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                       np.min(k[:,1]), np.max(k[:,1]), 
                                       np.min(k[:,2]), np.max(k[:,2])])
                    Pscales = np.vstack((Pscales, valtab))
                    Allcoors = np.vstack((Allcoors, k))
                elif Rotxis[c] == 'y':
                    k = castestrot3y(j.reshape(-1,3), Theta[c]*i)
                    ax.plot(k[:,0],k[:,1],k[:,2], linewidth=2, color='black')
                    valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                       np.min(k[:,1]), np.max(k[:,1]), 
                                       np.min(k[:,2]), np.max(k[:,2])])
                    Pscales = np.vstack((Pscales, valtab))
                    Allcoors = np.vstack((Allcoors, k))
                elif Rotxis[c] == 'z':
                    k = castestrot3z(j.reshape(-1,3), Theta[c]*i)
                    ax.plot(k[:,0],k[:,1],k[:,2], linewidth=2, color='black')
                    valtab = np.array([np.min(k[:,0]), np.max(k[:,0]), 
                                       np.min(k[:,1]), np.max(k[:,1]), 
                                       np.min(k[:,2]), np.max(k[:,2])])
                    Pscales = np.vstack((Pscales, valtab))
                    Allcoors = np.vstack((Allcoors, k))
        Allcoors = Allcoors[1:]
        Allx, Ally, Allz = Allcoors[:,0], Allcoors[:,1], Allcoors[:,2]
        Filledparts = np.array(list(zip(Allx, Ally, Allz)))
        Filled = np.vsplit(Filledparts, Rotn[c])
        for Fill in Filled:
            ax.add_collection3d(Poly3DCollection([Fill], facecolors='white')# add alpha for transparency settings
        Pscales = Pscales[1:]
        GrandCoords = np.array([Pscales[:,0].min(), Pscales[:,1].max(), 
                                Pscales[:,2].min(), Pscales[:,3].max(), 
                                Pscales[:,4].min(), Pscales[:,5].max()])
        GrandControl = np.vstack((GrandControl, GrandCoords))
    GrandControl = GrandControl[1:]
    xi = GrandControl[:,0].min()
    xa = GrandControl[:,1].max()
    yi = GrandControl[:,2].min()
    ya = GrandControl[:,3].max()
    zi = GrandControl[:,4].min()
    za = GrandControl[:,5].max()
    del GrandControl
    centre = np.array([xi+xa, yi+ya, zi+za])/2
    line = max((xa - xi),(ya - yi),(za - zi))*(0.6/2)
    ax.set_xlim((centre[0] - line), (centre[0] + line))
    ax.set_ylim((centre[1] - line), (centre[1] + line))
    ax.set_zlim((centre[2] - line), (centre[2] + line))
    # plt.axis('off') # Optional lack of axis
    plt.show()
    return
