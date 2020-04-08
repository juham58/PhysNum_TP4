import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def prob_3_c_sr(h, R, Z, precision_voulue, omega):
    temps_debut = time.process_time()

    # Constants
    M = R * h  # nombre de quadrillés en r
    N = Z * h  # nombre de qudrillés en h
    precision_voulue = precision_voulue

    # Création des array de potentiel
    V = np.zeros((M + 1, N + 1), float)
    Vprime = np.empty([M + 1, N + 1], float)

    # Définition des conditions frontières
    V[0:1 * h, 2*h : -1*h] = 150  # 1 cm fois h pour le cylindre du centre
    V[-1, :] = 0  # extrémité du cylindre en r=10cm (pour tout z pour ne pas briser la loop avec les voisins de r=10 inexistants)
    V[8*h:, 10*h], V[4*h:8*h, 22*h] = 0, 0  # extrémités intérieures (beigne) nulles
    V[8*h, 10*h : 22*h+1], V[4*h, 22*h:] = 0, 0  # extrémité des cylindres centraux en r=8 cm et r=4 cm
    V[:, 0], V[:, -1] = 0, 0  # extrémités en z=0 et z=30 cm

    # Main loop
    delta = 1.0
    compteur = 0
    Vprime[:] = V
    # print("h: ", h, "M: ", M)
    while delta > precision_voulue:
        compteur += 1

        # Calcul des nouvelles valeurs de potentiel
        for i in range(M + 1):
            for j in range(N + 1):
                if i < 1 * h and 2 * h < j < 32 * h:
                    Vprime[i, j] = Vprime[i, j]

                elif j == 0:
                    Vprime[i, j] = Vprime[i, j]

                elif j == N:
                    Vprime[i, j] = Vprime[i, j]

                elif i == M:
                    Vprime[i, j] = Vprime[i, j]

                elif j == 10 * h and i >= 8 * h:
                    Vprime[i, j] = Vprime[i, j]

                elif j == 22 * h and i >= 4 * h:
                    Vprime[i, j] = Vprime[i, j]

                elif i == 8 * h and 10 * h <= j <= 22 * h:
                    Vprime[i, j] = Vprime[i, j]

                elif i == 4 * h and j >= 22 * h:
                    Vprime[i, j] = Vprime[i, j]

                elif i == 0:  # Équation spéciale pour r=0 (singularité)
                    Vprime[i, j] = (1 + omega) / 6 * (4 * Vprime[1, j] + Vprime[0, j + 1] + Vprime[0, j - 1]) - omega * \
                                   Vprime[i, j]

                else:  # Équation standard
                    Vprime[i, j] = (1 + omega) / 4 * (h / (2 * i * h) * (Vprime[i + 1, j] - Vprime[i - 1, j])
                                                      + Vprime[i + 1, j] + Vprime[i - 1, j] + Vprime[i, j + 1] + Vprime[
                                                          i, j - 1]) - omega * Vprime[i, j]

        # Calcul le max de différence entre nouvelles et vieilles valeurs
        delta = np.max(abs(V - Vprime))
        print("compteur: ", compteur, "delta: ", delta)

        # On échange les deux array pour recommencer
        V[:] = Vprime[:]

    # On plot un plan 2D et on print le compteur d'itérations
    temps_fin = time.process_time()
    delta_temps = temps_fin - temps_debut
    print("Temps d'éxécution: ", delta_temps, "s")
    print("Nombre d'itération: ", compteur, " itérations")
    plt.figure(figsize=(9, 6))
    plt.imshow(Vprime, cmap="viridis")
    plt.axis()
    plt.colorbar(fraction=0.047, pad=0.04)
    plt.show()


prob_3_c_sr(10, 10, 33, 1e-7, 0.9425)
