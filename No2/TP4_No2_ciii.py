import matplotlib.pyplot as plt
from TP4_No2_b import prob_2
from TP4_No2_ci import prob_2_gs
from TP4_No2_cii import prob_2_sr

algo_base = prob_2(10, 10, 30, 1e-3, show=False)
gauss_seidel = prob_2_gs(10, 10, 30, 1e-3, show=False)
surrelaxation = prob_2_sr(10, 10, 30, 1e-3, 0.9425, show=False)


plt.figure(figsize=(16, 8))
plt.xscale("log")
plt.yscale("log")
plt.title("Plus grande variation de potentiel par itération en fonction du nombre d'itérations\npour les 3 algorithmes du numéro 2 avec h=10 et une précision de 0.001 cm")
plt.xlabel("Nombre d'itérations")
plt.ylabel("Plus grande variation de potentiel par itération [V]")
plt.plot(algo_base[0], algo_base[1], "-b", label="Algorithme de base")
plt.plot(gauss_seidel[0], gauss_seidel[1], "-r", label="Gauss-Seidel")
plt.plot(surrelaxation[0], surrelaxation[1], "-g", label="Surrelaxation")
plt.legend()
plt.grid()
#plt.show()

plt.figure(figsize=(16, 8))
plt.xscale("log")
plt.yscale("log")
plt.title("Plus grande variation de potentiel par itération en fonction du nombre d'itérations\npour les 3 algorithmes du numéro 2 avec h=10 et une précision de 0.001 cm")
plt.xlabel("Nombre d'itérations")
plt.ylabel("Plus grande variation de potentiel par itération [V]")
plt.plot(algo_base[0], algo_base[1], "-b", label="Algorithme de base")
plt.plot(gauss_seidel[0], gauss_seidel[1], "-r", label="Gauss-Seidel")
plt.plot(surrelaxation[2], surrelaxation[1], "-g", label="Surrelaxation")
plt.legend()
plt.grid()
plt.show()
