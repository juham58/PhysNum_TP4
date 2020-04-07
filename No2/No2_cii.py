import numpy as np
from pylab import imshow, show, plasma


def prob_2_sr(h, R, Z, precision_voulue, omega):
    # Constants
    M = R*h  # nombre de quadrillés en r
    N = Z*h  # nombre de qudrillés en h
    precision_voulue = precision_voulue

    # Création des array de potentiel
    V = np.zeros((M+1, N+1), float)
    Vprime = np.empty([M+1, N+1], float)

    # Définition des conditions frontières
    V[0:1*h, :] = 150  # 1 cm fois h pour le cylindre du centre
    V[-1, :] = 0  # extrémité du cylindre en r=10cm
    V[1*h:, 0], V[1*h:, -1] = 0, 0  # extrémités en z=0 et z=30 cm

    # Main loop
    delta = 1.0
    compteur = 0
    while delta > precision_voulue:
        compteur += 1

        # Calcul des nouvelles valeurs de potentiel
        for i in range(M+1):
            for j in range(N+1):

                if i < 1*h or i == M or j == 0 or j == N:  # si cond. frontières
                    Vprime[i, j] = V[i, j]

                else:
                    Vprime[i, j] = (1+omega)/4*(h/(2*i*h)*(V[i+1, j]-V[i-1, j])
                        + V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1]) - omega*(V[i, j])

        # Calcul le max de différence entre nouvelles et vieilles valeurs
        delta = np.max(abs(V-Vprime))
        print("compteur: ", compteur, "delta: ", delta)

        # On échange les deux array pour recommencer
        V, Vprime = Vprime, V

    # Make a plot
    imshow(V)
    plasma()
    show()


prob_2_sr(10, 10, 30, 1e-1, 0) # 0 c'est pour le cas sans surrelaxation
