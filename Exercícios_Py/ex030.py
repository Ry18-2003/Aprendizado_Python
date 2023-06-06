# Par ou ímpar

a1 = int(input('Número: '))

print('O número digitado é ', end='')  # Junção com a resposta

if a1 % 2 != 0:  # Verificação do resto da divisão
    print('ímpar.')
else:
    print('par.')
