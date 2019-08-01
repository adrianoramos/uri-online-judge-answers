# 1017 - Gasto de Combustível

LKM = 12

tempo = int(input())
kmh = int(input())

distancia = tempo * kmh
combustivel = distancia / LKM

print("%0.3f" % combustivel)