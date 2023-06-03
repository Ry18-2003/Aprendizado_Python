# ler quatro nomes e sortear 1

from random import choice

# choice seleciona uma variável aleatória

a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))

# utilizar colchetes [] dentro do parentese no choice

print(f'O aluno sorteado foi {choice([a1, a2, a3, a4])}')

"""
import random

# Variáveis disponíveis
var1 = 'a'
var2 = '20'
var3 = '30'

# Selecionar uma variável aleatória
selected_variable = random.choice([var1, var2, var3])

print(selected_variable)
"""