# Desigualdade triangular.

a1 = float(input('1° Valor: '))
a2 = float(input('2° Valor: '))
a3 = float(input('3° Valor: '))

if a1 + a2 > a3 and a3 + a1 > a2 and a2 + a3 > a1:
    print('Sim é possível formar um triangulo com esses valores.')
else:
    print('Não é possível formar um triangulo com esses valores.')
