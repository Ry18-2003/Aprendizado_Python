# Preço de viagem

a1 = float(input('Qual a distancia a percorrer: '))

print(f'Para a distancia de {a1:.1f} km, o preço da viagem vai ser de R$', end='')

if a1 > 200:
    print(f'{a1 * 0.45:.2f}.')
else:
    print(f'{a1 * 0.50:.2f}.')
