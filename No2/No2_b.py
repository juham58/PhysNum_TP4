import numpy as np
from pylab import imshow,gray,show


def prob_2(h, R, Z, precision_voulue):
    # Constants
    M = R*h  # nombre de quadrillés en r
    N = Z*h  # nombre de qudrillés en h
    precision_voulue = precision_voulue

    # Create arrays to hold potential values
    pot = np.zeros((M+1,N+1), float)
    pot[0:1*h, :] = 150  # 1 cm fois h pour le cylindre du centre
    pot[-1, :] = 0  # extrémité du cylindre en r=10cm
    pot[1*h:, 0], pot[1*h:, -1] = 0, 0 # extrémités en z=0 et z=30 cm
    potprime = np.empty([M+1,N+1],float)

    # Main loop
    delta = 1.0
    while delta > precision_voulue:

        # Calculate new values of the potential
        for i in range(M+1):
            for j in range(N+1):

                if i < 1*h or i == M or j == 0 or j == N:  # si cond. frontières
                    potprime[i, j] = pot[i, j]

                else:
                    potprime[i, j] = 1/4*(h/(2*i*h)*(pot[i+1, j]-pot[i-1, j]) \
                        + pot[i+1, j] + pot[i-1, j] + pot[i, j+1] + pot[i, j-1])

        # Calculate np.maximum difference from old values
        delta = np.max(abs(pot-potprime))
        print(delta)

        # Swap the two arrays around
        pot,potprime = potprime,pot

    # Make a plot
    imshow(pot)
    gray()
    show()


prob_2(10, 10, 30, 2e-2)
