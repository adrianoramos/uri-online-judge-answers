ln = input()

num1, num2, num3 = [int(x) for x in ln.split(' ')]

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print("%d\n%d\n%d" % (num1, num2, num3))
    else:
        print("%d\n%d\n%d" % (num1, num3, num2))

if num2 < num1 and num2 < num3:
    if num1 < num3:
        print("%d\n%d\n%d" % (num2, num1, num3))
    else:
        print("%d\n%d\n%d" % (num2, num3, num1))

if num3 < num1 and num3 < num2:
    if num1 < num2:
        print("%d\n%d\n%d" % (num3, num1, num2))
    else:
        print("%d\n%d\n%d" % (num3, num2, num1))

print("\n%d\n%d\n%d" % (num1, num2, num3))