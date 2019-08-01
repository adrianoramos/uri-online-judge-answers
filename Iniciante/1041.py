# 1041 - Coordenadas de um Ponto

ln = input()

coord1, coord2 = ln.split(" ")

x = float(coord1)
y = float(coord2)

if x == 0 and y == 0:
    print("Origem")
elif x != 0 and y == 0:
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")

if x > 0:
    if y > 0:
        print("Q1")
    elif y < 0:
        print("Q4")
elif x < 0:
    if y > 0:
        print("Q2")
    elif y < 0:
        print("Q3")