# 1036 - Fórmula de Baskhara

entrada = input()

valores = [float(v) for v in entrada.split(" ")]
delta = (valores[1] ** 2) - (4 * valores[0] * valores[2])

if delta > 0 and valores[0] > 0:
    raiz1 = (valores[1] * -1 + delta ** (float(1)/2)) / (2 * valores[0])
    raiz2 = (valores[1] * -1 - delta ** (float(1)/2)) / (2 * valores[0])

    print("R1 = {0:.5f}\nR2 = {1:.5f}".format(raiz1, raiz2))
else:
    print("Impossivel calcular")
