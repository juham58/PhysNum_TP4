import numpy as np
import datetime
import matplotlib.pyplot as plt


def prob_2_gs(h, R, Z, precision_voulue, omega):

    # Constants
    M = R*h  # nombre de quadrillés en r
    N = Z*h  # nombre de qudrillés en h
    precision_voulue = precision_voulue

    # Création des array de potentiel
    V = np.zeros((M+1, N+1), float)
    Vprime = np.empty([M+1, N+1], float)

    # Définition des conditions frontières
    V[0:1 * h, 3 * h:-3 * h] = 150  # 1 cm fois h pour le cylindre du centre
    V[-1, :9 * h], V[-1, -9 * h:] = 0, 0  # extrémité du cylindre en r=10cm
    V[5 * h:, 9 * h], V[5 * h:, 21 * h] = 0, 0  # extrémités intérieures (beigne) nulles
    V[5 * h, 9 * h:21 * h] = 0  # extrémité du cylindre central en r=5 cm
    V[:, 0], V[:, -1] = 0, 0  # extrémités en z=0 et z=30 cm

    # Main loop
    delta = 1.0
    compteur = 0
    Vprime[:] = V
    #print("h: ", h, "M: ", M)
    while delta > precision_voulue:
        compteur += 1

        # Calcul des nouvelles valeurs de potentiel
        for i in range(M+1):
            for j in range(N+1):
                if i < 1*h and 3*h < j < 27*h:  # conditions frontières.
                    Vprime[i, j] = Vprime[i, j]

                elif j == 0:
                    Vprime[i, j] = Vprime[i, j]

                elif j == N:
                    Vprime[i, j] = Vprime[i, j]

                elif j == 9*h and i >= 5*h:
                    Vprime[i, j] = Vprime[i, j]

                elif j == 21*h and i >= 5*h:
                    Vprime[i, j] = Vprime[i, j]

                elif i == M:
                    Vprime[i, j] = Vprime[i, j]

                elif i == 5*h and 9 * h <= j <= 21 * h:
                    Vprime[i, j] = Vprime[i, j]

                elif i == 0:
                    Vprime[i, j] = (1+omega)/6 * (4*Vprime[1, j] + Vprime[0, j+1] + Vprime[0, j-1]) - omega*Vprime[i, j]

                else:
                    Vprime[i, j] = (1+omega)/4*(h/(2*i*h)*(Vprime[i+1, j]-Vprime[i-1, j])
                        + Vprime[i+1, j] + Vprime[i-1, j] + Vprime[i, j+1] + Vprime[i, j-1])-omega*Vprime[i, j]

        # Calcul le max de différence entre nouvelles et vieilles valeurs
        delta = np.max(abs(V-Vprime))

        # On échange les deux array pour recommencer
        print("compteur: ", compteur, "delta: ", delta)
        V[:] = Vprime[:]
    # On print le compteur lorsque la précision est atteinte pour trouver le meilleur omega
    print("compteur: ", compteur, "delta: ", delta)
    plt.figure(figsize=(9, 6))
    plt.imshow(Vprime, cmap="viridis")
    plt.axis()
    plt.colorbar(fraction=0.047, pad=0.04)
    plt.show()

prob_2_gs(10,10,30,1e-3,0.9)
