# Ler a velocidade de um carro, e multar ele se ele passar de 80 km/h
# Multa de R$7.00, por cada km a mais que o permitido.

a1 = float(input('Velocidade do veiculo: '))
if a1 > 80:
    a1 = (a1-80) * 7
    print(f'Você foi multado em R${a1:.2f}')

print('Tenha um bom dia.')
