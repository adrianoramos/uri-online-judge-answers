# 1038 - Lanche

entrada = input()

codigo = int(entrada.split(" ")[0])
quantidade = int(entrada.split(" ")[1])
total = 0

if codigo == 1:
    total = quantidade * 4.0
elif codigo == 2:
    total = quantidade * 4.5
elif codigo == 3:
    total = quantidade * 5.0
elif codigo == 4:
    total = quantidade * 2.0
elif codigo == 5:
    total = quantidade * 1.5

print("Total: R$ {0:.2f}".format(total))