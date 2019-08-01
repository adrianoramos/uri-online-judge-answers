# 1020 - Idade em Dias

ANO=365
MES=30

dias = int(input())
anos = dias // ANO
dias -= anos * ANO
meses = dias // MES
dias -= meses * MES

print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % dias)