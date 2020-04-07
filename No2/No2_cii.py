import numpy as np
import datetime
import matplotlib.pyplot as plt


def prob_2_gs(h, R, Z, precision_voulue, omega):
    temps_debut = datetime.datetime.now()

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
    Vprime[:] = V
    #print("h: ", h, "M: ", M)
    while delta > precision_voulue:
        compteur += 1

        # Calcul des nouvelles valeurs de potentiel
        for i in range(M+1):
            for j in range(N+1):

                if i < 1*h or i == M or j == 0 or j == N:  # si cond. frontières
                    Vprime[i, j] = Vprime[i, j]

                else:
                    Vprime[i, j] = (1+omega)/4*(h/(2*i*h)*(Vprime[i+1, j]-Vprime[i-1, j])
                        + Vprime[i+1, j] + Vprime[i-1, j] + Vprime[i, j+1] + Vprime[i, j-1])-omega*Vprime[i, j]

        # Calcul le max de différence entre nouvelles et vieilles valeurs
        delta = np.max(abs(V-Vprime))

        # On échange les deux array pour recommencer
        V[:] = Vprime[:]
    # On print le compteur lorsque la précision est atteinte pour trouver le meilleur omega
    print("compteur: ", compteur, "delta: ", delta)


prob_2_gs(10, 10, 30, 1e-2, 0.93)
prob_2_gs(10, 10, 30, 1e-2, 0.9425)
prob_2_gs(10, 10, 30, 1e-2, 0.9429)
prob_2_gs(10, 10, 30, 1e-2, 0.9433)
prob_2_gs(10, 10, 30, 1e-2, 0.95)
prob_2_gs(10, 10, 30, 1e-2, 0)

