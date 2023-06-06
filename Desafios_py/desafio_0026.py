# Fazer o computador pensar em um número de 0 a 5 e ver se o usuário adivinha.

from random import randint

a1 = randint(0, 5)

print('Pensando em um número entre 0 e 5...')
a2 = int(input('Pronto, tente adivinhar: '))

if a1 == a2:
    print('Você acertou!!!')
else:
    print(f'Você errou! O número que pensei é {a1}')
