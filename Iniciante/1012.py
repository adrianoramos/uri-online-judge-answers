# 1012 - Área

pi = 3.14159

def parse(line):
  ln = line.split(' ')
  return float(ln[0]), float(ln[1]), float(ln[2])

a, b, c = parse(input())

triangulo = (a * c) / 2
circulo = pi * (c**2)
trapezio = ((a + b) * c) / 2
quadrado = b**2
retangulo = a*b

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)