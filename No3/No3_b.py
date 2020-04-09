import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def prob_3_b_sr(h, R, Z, precision_voulue, omega):
    temps_debut = time.process_time()

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

    # Boucle principale
    delta = 1.0
    compteur = 0
    Vprime[:] = V
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

                elif i == 0: # Équation spéciale pour r=0 (singularité)
                    Vprime[i, j] = (1+omega)/6 * (4*Vprime[1, j] + Vprime[0, j+1] + Vprime[0, j-1]) - omega*Vprime[i, j]

                else: # Équation standard
                    Vprime[i, j] = (1+omega)/4*(h/(2*i*h)*(Vprime[i+1, j]-Vprime[i-1, j])
                        + Vprime[i+1, j] + Vprime[i-1, j] + Vprime[i, j+1] + Vprime[i, j-1])-omega*Vprime[i, j]

        # Calcul le max de différence entre nouvelles et vieilles valeurs
        delta = np.max(abs(V-Vprime))

        # On échange les deux array pour recommencer
        V[:] = Vprime[:]

    # On plot un plan 2D et on print le compteur d'itérations
    temps_fin = time.process_time()
    delta_temps = temps_fin - temps_debut
    print("Temps d'exécution: ", delta_temps, "s")
    print("Nombre d'itération: ", compteur, " itérations")

    plt.figure(figsize=(9, 6))
    ax = plt.gca()
    im = ax.imshow(Vprime, cmap="viridis")
    plt.xlabel("Position en {}z [cm]".format(h))
    plt.ylabel("Position en {}r [cm]".format(h))
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.2)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label('Potentiel [V]', labelpad=15, rotation=270)
    plt.show()


prob_3_b_sr(10, 10, 30, 1e-3, 0.9425)
