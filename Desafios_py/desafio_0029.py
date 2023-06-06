# ler a distância da viagem em km e mostrar o preço da passagem.
# Caso acima de 200 km, a passagem passa a ser R$0.45 caso abaixo a passagem é de R$0.50

a1 = float(input('Digite a distancia da viagem: '))
print(f'Para a viagem de {a1:.1f} km, vai ser necessário pagar o valor de R$', end="")
print(f'{a1 * 0.50:.2f}' if a1 <= 200 else f'{a1 * 0.45:.2f}')
