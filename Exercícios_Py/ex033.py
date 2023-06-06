# 3 valores, mostrar o maior e o menor.

a1 = int(input('1° Valor: '))
a2 = int(input('2° Valor: '))
a3 = int(input('3° Valor: '))

if a1 == a2 and a3 == a1 and a2 == a3:
    print('São valores iguais.')
else:
    b1 = a1
    b2 = a1
    # Maior
    if a2 > a1 and a2 > a3:
        b1 = a2
    if a3 > a1 and a3 > a2:
        b1 = a3
    # Menor
    if a2 < a1 and a2 < a3:
        b2 = a2
    if a3 < a1 and a3 < a2:
        b2 = a3

    print(f'O maior valor é {b1}')
    print(f'O menor valor é {b2}')

    # print(f'O maior valor digitado foi: {max(a1, a2, a3)}')
    # print(f'O menor valor digitado foi: {min(a1, a2, a3)}')
