# Programa para ler um número e separar em unidade, dezena, centena e milhar.

"""
a1 = str(input('Número de 0 a 9999: '))
a1 = '0000' + a1
a2 = len(a1)

print(f'O número digitado foi: {a1[4:]}\nUnidades: {a1[a2-1]}\nDezenas: {a1[a2-2]}\nCentena: {a1[a2-3]}\n'
      f'Milhar: {a1[a2-4]}')
"""
a1 = int(input('Número de 0 a 9999: '))

print(f'O número digitado foi: {a1}\nUnidades: {a1 % 10}\nDezenas: {(a1//10)%10}\nCentena: {(a1//100)%10}\nMilhar: {(a1//1000)%10}')
