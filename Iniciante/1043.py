ln = input()

a, b, c = [float(x) for x in ln.split()]

if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
    print("Perimetro = {:.1f}".format(a+b+c))
else:
    print("Area = {:.1f}".format(((a+b)/2) * c))