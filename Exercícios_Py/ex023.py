# Ler um número e separar em unidade, dezena, centena e milhar.
"""
# a1 int para aceitar apenas números
a1 = int(input('Enter a number: '))
# a1 str para transformar em string
a1 = str(a1)
# 0000 para completar todos os parâmetros
a1 = '0000' + a1
# para exibir apenas os 4 últimos números
print(f'The number entered, up to thousands is {a1[-4:]}.'
      f'\nIt has {a1[-1:]} units.\nIt has {a1[-2:-1]} tens.\n'
      f'It has {a1[-3:-2]} hundreds.\nIt has {a1[-4:-3]} thousands.')
"""  # versão em str

a1 = int(input('Enter a number: '))

print(f'The number entered is {a1}.\n'
      f'It has {a1%10} units.\n'
      f'It has {a1//10%10} tens.\n'
      f'It has {a1//100%10} hundreds.\n'
      f'It has {a1//1000%10} thousands.')
