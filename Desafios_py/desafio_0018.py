# ler quatro alunos e indicar a ordem de apresentação deles.

from random import sample

a1 = str(input('Primeiro: '))
a2 = str(input('Segundo: '))
a3 = str(input('Terceiro: '))
a4 = str(input('Quarto: '))

a5 = a1, a2, a3, a4
# O comando sample vai me dar uma amostra aleatória sem repetição de uma sequência
a6 = sample(a5, k=4)

print(f'A ordem de apresentação vai ser: {a6[0]}, {a6[1]}, {a6[2]} e {a6[3]}')
