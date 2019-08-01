# 1040 - Média 3

ln = input("")

nota1, nota2, nota3, nota4 = [float(x) for x in ln.split(" ")]
peso1, peso2, peso3, peso4 = 2, 3, 4, 1

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)

if (media >= 7):
    print("Media: {0:.1f}".format(media))
    print("Aluno aprovado.")
  
elif (media >= 5):
    print("Media: {0:.1f}".format(media))
    print("Aluno em exame.")
    
    exame = input()
    exame = float(exame)
    
    media_exame = (media + exame) / 2
    
    if (media_exame >= 5):
        print("Nota do exame: {0:.1f}".format(exame))
        print("Aluno aprovado.")
        print("Media final: {0:.1f}".format(media_exame))
    else:
        print("Nota do exame: {0:.1f}".format(exame))
        print("Aluno reprovado.")
        print("Media final: {0:.1f}".format(media_exame))

else:
    print("Media: {0:.1f}".format(media))
    print("Aluno reprovado.")