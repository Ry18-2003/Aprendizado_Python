# ler um ano e mostrar se ele é bissexto

a1 = int(input('Digite o ano: '))

if a1 % 4 == 0 and (a1 % 100 != 0 or a1 % 400 == 0):
    print(f'{a1} é um ano Bissexto!')
else:
    print(f'{a1} não é um ano Bissexto!')
