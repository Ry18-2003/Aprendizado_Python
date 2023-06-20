# Desigualdade Triangular +

a1 = float(input('1° Lado do triangulo: '))
a2 = float(input('2° Lado do triangulo: '))
a3 = float(input('3° Lado do triangulo: '))

if a1 + a2 > a3 and a2 + a3 > a1 and a3 + a1 > a2:
    print('É possivel formar um triângulo ',end='')
    if a1 == a2 == a3:
        print('Equilátero.')

    elif a1 == a2 or a3 == a1 or a2 == a3:
        print('Isósceles')
    
    else:
        print('Escaleno')

else:
    print('Não é possivel formar um triângulo com esses valores.')