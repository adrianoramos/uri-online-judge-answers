# 1015 - Distância Entre Dois Pontos

def parse(line):
  l = line.split(' ')
  return float(l[0]), float(l[1])

x1, y1 = parse(input())
x2, y2 = parse(input())

distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print("%.4f" % distance)