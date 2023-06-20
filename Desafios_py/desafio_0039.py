# Atribuição de categoria em natação

from datetime import datetime

a1 = int(input('Insira o ano de nascimento do nadador: '))

if datetime.now().year - a1 <= 9:
    a2 = 'MIRIN'
elif datetime.now().year - a1 <= 14:
    a2 = 'INFANTIL'
elif datetime.now().year - a1 <= 19:
    a2 = 'JUNIOR'
elif datetime.now().year - a1 <= 20:
    a2 = 'SÉNIOR'
else:
    a2 = 'MASTER'

print(f'A categoria do nadador é: {a2} {datetime.now().year - a1}')
