# Desigualdade triangular

a1 = float(input('1° valor: '))
a2 = float(input('2° valor: '))
a3 = float(input('3° valor: '))

if a1 + a2 > a3 and a2 + a3 > a1 and a3 + a1 > a2:
    print('É possível formar um triangulo.')
else:
    print('Não é possível formar um triangulo.')
