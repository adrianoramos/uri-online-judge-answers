# 1010 - Cálculo Simples

def calculate(piece):
    return float(piece[1] * piece[2])
    
def parse(line):
    ln = line.split(' ')
    code = int(ln[0])
    qnty = int(ln[1])
    value = float(ln[2])
    return code, qnty, value

piece_1 = parse(input())
piece_2 = parse(input())

total = calculate(piece_1) + calculate(piece_2)

print("VALOR A PAGAR: R$ %.2f" % total)