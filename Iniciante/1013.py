# 1013 - O Maior

def parse(line):
  l = line.split(' ')
  return int(l[0]), int(l[1]), int(l[2])

a, b, c = parse(input())

m = ((a+b)+abs(a-b)) / 2
m = ((m+c)+abs(m-c)) /2

print("%d eh o maior" % m)