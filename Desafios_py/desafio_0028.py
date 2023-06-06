# Ler um número e mostre se ele é par ou impar

a1 = int(input('Escreva um número: '))
print('O número que você digitou é: ', end='')
print('Par' if a1 % 2 == 0 else 'Impar')
