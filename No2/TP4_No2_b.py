import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def prob_2(h, R, Z, precision_voulue, show=True):
    temps_debut = time.process_time()

    # Constantes
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

    # Boucle principale
    delta = 1.0
    compteur = 0
    liste_compteur = []
    liste_delta = []
    liste_delta_temps = []
    while delta > precision_voulue:
        compteur += 1

        # Calcul des nouvelles valeurs de potentiel
        for i in range(M+1):
            for j in range(N+1):

                if i < 1*h or i == M or j == 0 or j == N:  # si cond. frontières
                    Vprime[i, j] = V[i, j]

                else:
                    Vprime[i, j] = 1/4*(h/(2*i*h)*(V[i+1, j]-V[i-1, j])
                        + V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1])

        # Calcul le max de différence entre nouvelles et vieilles valeurs
        delta = np.max(abs(V-Vprime))
        temps_maintenant = time.process_time()

        # Récolte des données pour le 2ciii
        liste_compteur.append(compteur)
        liste_delta.append(delta)
        liste_delta_temps.append(temps_maintenant)

        # On échange les deux array pour recommencer
        V, Vprime = Vprime, V

    # Calcul du temps d'exécution
    temps_fin = time.process_time()
    delta_temps = temps_fin - temps_debut

    # Mise en place de la sortie
    print("Temps d'éxécution: ", delta_temps, "s")
    print("Nombre d'itération: ", compteur, " itérations")
    if show is True:
        plt.figure(figsize=(9, 6))
        ax = plt.gca()
        im = ax.imshow(Vprime, cmap="viridis")
        plt.title("Potentiel du problème 2 avec h={} et une précision de {} V\navec l'algorithme de base".format(h, precision_voulue))
        plt.xlabel("Position en {}z [cm]".format(h))
        plt.ylabel("Position en {}r [cm]".format(h))
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.2)
        cbar = plt.colorbar(im, cax=cax)
        cbar.set_label('Potentiel [V]', labelpad=15, rotation=270)
        plt.show()
    return liste_compteur, liste_delta, liste_delta_temps


prob_2(10, 10, 30, 1e-4)
