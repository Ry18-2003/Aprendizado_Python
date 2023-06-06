# Jogo de adivinhação de número

from random import randint
from time import sleep
a1 = randint(0, 5)

print(f'{"=-"*20}=\nPensando em um número entre 0 e 5...\n{"=-"*20}=')
print("A PENSAR...")
sleep(2)
a2 = int(input('Qual o número? '))

print('Acertou!' if a1 == a2 else 'Errou!')