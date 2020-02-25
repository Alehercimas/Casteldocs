# Higher level compound function allowing for multiple rotations

def manyrots(P, Cp, n):# The input n determines the amount of rotations
    pis = np.linspace(0, np.pi*2, n)
    for i in pis:
        castelsimprot(P, Cp, i)
