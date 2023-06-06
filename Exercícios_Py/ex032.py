# Ano Bissexto

from datetime import date

a1 = int(input('Digite o ano: [0 para o ano atual] '))
if a1 == 0:
    a1 = date.today().year

print('É um ano bissexto!' if a1 % 4 == 0 and (a1 % 100 != 0 or a1 % 400 == 0) else 'Não é um ano bissexto!')
