# Programa para informar se o joven ainda, deve ou já passou da idade de se apresentar. Tbm falar em quantos anos ele ainda tem antes.

from datetime import datetime

a1 = int(input('Ano de nascimento: '))
b1 = datetime.now().year


if b1 - a1 == 18:
    print("Você deve procurar um quarteu para se alistar.")

elif b1 - a1 > 18:
    print(f'Você já passou da idade de alistamento a {b1-a1-18} anos.')

else:
    print(f'Você ainda tem {18 - (b1 - a1)} ano(s) até o alistamento.')
