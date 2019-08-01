# 1035 - Teste de Seleção 1

valores = input()
numeros = [int(n) for n in valores.split(" ")]

if numeros[1] > numeros[2] and \
    numeros[3] > numeros[0] and \
    numeros[2] + numeros[3] > numeros[0] + numeros[1] and \
    (numeros[2] > 1 and numeros[3] > 1) and \
    numeros[0] % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
