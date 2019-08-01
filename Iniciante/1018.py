# 1018 - Cédulas

valor_notas = [100, 50, 20, 10, 5, 2, 1]

valor = int(input())

print(valor)

for valor_nota in valor_notas:
        qtde_nota = valor // valor_nota
        valor -= qtde_nota * valor_nota
        print(("%d nota(s) de R$ %0.2f" % (qtde_nota, valor_nota)).replace('.',','))