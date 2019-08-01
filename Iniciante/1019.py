# 1019 - Conversão de Tempo

HORA = 3600
MINUTO = 60

tempo = int(input())

horas = tempo // HORA
tempo -= horas * HORA
minutos = tempo // MINUTO
tempo -= minutos * MINUTO
segundos = tempo

print("%d:%d:%d" % (horas, minutos, segundos))