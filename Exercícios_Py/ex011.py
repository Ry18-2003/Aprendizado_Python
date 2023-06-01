# calcular área e quantos litros de tinta são necessários para pintar uma parede (1 litro pinta 2 m²)

a1 = float(input('Altura da parede: '))
a2 = float(input('Largura da parede: '))

print(f'Para pintar uma parede com {a1} X {a2}, totalizando a área de {a1*a2:.2f}m²\n'
      f'Vai precisar de {a1*a2/2:.2f}l de tinta')