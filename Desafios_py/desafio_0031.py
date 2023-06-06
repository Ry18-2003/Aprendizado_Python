# Ler 3 números e mostrar qual o maior e qual o menor.

a1 = int(input('1° número: '))
a2 = int(input('2° número: '))
a3 = int(input('3° número: '))
"""
if a1 == a2 == a3:
    print('São iguais')
else:
    if a1 == a2 or a1 == a3 or a2 == a3:
        print("Há dois valores iguais")

    if a1 >= a2 and a1 >= a3:
        print(f'Maior: {a1}')
    else:
        if a2 >= a1 and a2 >= a3:
            print(f'Maior: {a2}')
        else:
            if a3 >= a2 and a3 >= a1:
                print(f'Maior: {a3}')

    if not a1 > a2 and not a1 > a3:
        print(f'Menor:  {a1}')
    else:
        if not a2 > a1 and not a2 > a3:
            print(f'Menor: {a2}')
        else:
            if not a3 > a2 and not a3 > a1:
                print(f'Menor: {a3}')
"""  # Funciona, mas é muito grande

if a1 == a2 == a3:
    print('São iguais')
else:
    print(f'Maior: {max(a1, a2, a3)}')
    print(f'Menor: {min(a1, a2, a3)}')

