# Programa que leia a altura e a largura de uma parede e calcule quantos litros de tinta são necessários para pintala,
# sendo que cada litro de tinta pinta 2-m²

a1 = float(input('Digite a altura da parede: '))
a2 = float(input('Digite a largura da parede: '))

print(f'Uma parede com {a1*a2:.2f}m², vai precisar de {(a1*a2)/2:.2f} litros de tinta.')
