# Triangulos

a1 = float(input('1° Lado: '))
a2 = float(input('2° Lado: '))
a3 = float(input('3° Lado: '))

if a1 + a2 > a3 and a2 + a3 > a1 and a3 + a1 > a2:
    if a1 == a2 == a3:
        a4 = 'EQUILATERO'
    
    elif a1 == a2 or a2 == a3 or a3 == a1:
        a4 = 'ISÓCELES'
    
    else:
        a4 = 'ESCALENO'

    print(f'É possivel formar um triângulo {a4}.')

else:
    print('Não é possivel formar um triângulo.')
