# Clasificando atletas


from datetime import date

a1 = int(input('Digite seu ano de nascimento: '))
a2 = date.today().year - a1
if a2 > -1:
    if a2 < 10:
        a3 = 'MIRIM'

    elif a2 < 15:
        a3 = 'INFANTIL'

    elif a2 < 20:
        a3 = 'JÚNIOR'

    elif a2 < 26:
        a3 = 'SENIOR'
        
    else:
        a3 = 'MASTER'

    print(f'A categoria a que esse nadador pertence é a {a3}')

else:
    print('Idade Invalida!')
