import numpy as np
import time
import matplotlib.pyplot as plt


def prob_2_sr(h, R, Z, precision_voulue, omega, show=True):
    temps_debut = time.process_time()

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

    liste_compteur = []
    liste_delta = []
    liste_delta_temps = []
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
        temps_maintenant = time.process_time()
        print("compteur: ", compteur, "delta: ", delta, "temps:", temps_maintenant-temps_debut)

        liste_compteur.append(compteur)
        liste_delta.append(delta)
        liste_delta_temps.append(temps_maintenant-temps_debut)

        # On échange les deux array pour recommencer
        V[:] = Vprime[:]

    # Make a plot
    temps_fin = time.process_time()
    delta_temps = temps_fin - temps_debut
    print("Temps d'éxécution: ", delta_temps, " s")
    print("Nombre d'itération: ", compteur, " itérations")
    if show is True:
        plt.figure(figsize=(9, 6))
        plt.imshow(Vprime, cmap="viridis")
        plt.title("Potentiel du problème 2 avec h={} et une précision de {} V".format(h, precision_voulue))
        plt.axis()
        plt.colorbar()
        plt.show()
    return liste_compteur, liste_delta, liste_delta_temps


#prob_2_sr(10, 10, 30, 1e-5, 0.9)
