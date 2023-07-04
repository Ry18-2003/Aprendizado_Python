 # JOKEMPO

from random import randint
from time import sleep
print(f'{" JOGO DE PADRA PAPEL OU TESOURA (JOKENPÔ) ":=^80}')

print('''Escolha entre:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

a1 = int(input('Qual sua escolha: '))
a2 = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÓ')

if 0 <= a1 <= 2:
    b1 = ['PEDRA', 'PAPEL', 'TESOURA']
    b2 = ['VOCÊ PERDEU! Mais sorte na proxima!', 'VOCÊ VENCEU!', 'EMPATE!']

    print('='*40)
    print(f'MAQUINA: {b1[a2]}\nVOCÊ: {b1[a1]}')
    print('='*40)

    if a1 == a2:
        a3 = 2
    elif a1 == 0 and a2 == 2:
        a3 = 1
    elif a1 == 2 and a2 ==0:
        a3 = 0
    elif a1 == 1 and a2 == 0:
        a3 = 1
    elif a1 == 0 and a2 == 1:
        a3 = 0
    elif a1 == 2 and a2 == 1:
        a3 = 1
    elif a1 == 1 and a2 == 2:
        a3 = 0

    print(b2[a3])

else:
    print('Escolha invalida!')
