# Algumas formas de somar

"""
a1 = input('Digite um número: ')
a2 = input('Digite mais um número: ')
a3 = a1 + a2
                                                    
print('A soma entre {} e {} é {}. Correto?'.format(a1, a2, a3))
"""  # V1 errado, isso mostra a junção dos números em vez da soma

"""
a1 = int(input('Digite um número: '))
a2 = int(input('Digite mais um número: '))
a3 = a1 + a2

print(f'A soma de {a1} e {a2} é {a3}. Certo?')
"""  # v2 feito de forma correta, porem grande

a1 = int(input('Escreva um número: '))
a2 = int(input('Escreva mais um número: '))

print('A soma de {} e {} é de {}'.format(a1, a2, a1+a2))
