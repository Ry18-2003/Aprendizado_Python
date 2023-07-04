# Nota final

a1 = float(input('1° nota: '))
a2 = float(input('2° nota: '))

if (a1 + a2) / 2 < 5:
    print('Aluno REPROVADO!')

elif (a1 + a2) / 2 < 7:
    print('Aluno de RECUPERAÇÃO!')

else:
    print('Aluno APROVADO!')

