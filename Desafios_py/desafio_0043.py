# Jokenpo

from random import randint

a1 = 'PEDRA','PAPEL', 'TESOURA'

print('-/--/--/+Jokenpô+/--/--/-')

a2 = str(input('Vamos jogar jokenpô.\n3...\n2...\n1...\nJokenpô: ')).strip().upper()

if a2 != 'PEDRA' and a2 != 'PAPEL' and a2 != 'TESOURA':
    print('Insira PEDRA, PAPEL ou TESOURA. Parece até que não sabe jogar.')

else:
    a3 = a1[randint(0,2)]

    if a3 == 'PEDRA' and a2 == 'TESOURA':
        a4 = 0

    elif a2 == 'PEDRA' and a3 == 'TESOURA':
        a4 = 1

    elif a3 == 'TESOURA' and a2 == 'PAPEL':
        a4 = 0

    elif a2 == 'TESOURA' and a3 == 'PAPEL':
        a4 = 1

    elif a3 == 'PAPEL' and a2 == 'PEDRA':
        a4 = 0

    elif a2 == 'PAPEL' and a3 == 'PEDRA':
        a4 = 1
  
    else:
        a4 = -1

    print(f'\nPC: {a3}\nHUMANO: {a2}\n')
    
    if a4 == -1:
        print('Empate! Espero ganhar na proxima.')
    
    elif a4 == 0:
        print('VOCÊ PERDEU HUMANO!!!')

    else:
        print('Droga! É sua vitoria humano.')