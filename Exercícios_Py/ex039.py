# Verificar alistamento

from datetime import date

a1 = int(input('Ano de nascimento: '))
a2 = date.today().year - a1
if a2 == 18:
    print('Comparecer no quartel para o alistamento!')

elif a2 > 18:
    print(f'Você já passou do periodo de alistamento há {a2 - 18} anos. Seu ano de alistamento foi em {date.today().year - (a2 - 18)}.')

elif a2 < 18 and a2 > -1:
    print(f'Você vai ter que comparecer no quarteo em {18-a2} anos. Seu ano de alistamento vai ser em {date.today().year + (18-a2)}.')

else:
    print('Ano de nascimento invalido!')
