# Aumento de salário

a1 = float(input('Digite o salário: '))

print(f'O salário de R${a1:.2f} vai passar a ser R$', end='')

if a1 > 1250:
    print(f'{a1 * 1.10:.2f} com um aumento de 10%.')
else:
    print(f'{a1 * 1.15:.2f} com um aumento de 15%.')
