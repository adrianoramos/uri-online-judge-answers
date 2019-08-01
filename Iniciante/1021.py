# 1021 - Notas e Moedas

dinheiro = float(input())

if dinheiro >= 0 and dinheiro <= 1000000:
    
    dinheiro_valores = (100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01)
    total_por_nota = 0
    mensagem_notas, mensagem_moedas = False, False
    tipo = "nota"

    for nota in dinheiro_valores:
        if mensagem_notas == False and nota > 1:
            print("NOTAS:")
            mensagem_notas = True
        
        if mensagem_moedas == False and nota < 2:
            print("MOEDAS:")
            tipo = "moeda"
            mensagem_moedas = True

        quantidade_notas = int(dinheiro / nota)
        total_valor = quantidade_notas * nota
        dinheiro = round(dinheiro - total_valor, 2)
        
        print("{0} {1}(s) de R$ {2:.2f}".format(quantidade_notas, tipo, nota))