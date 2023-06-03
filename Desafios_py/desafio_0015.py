# ler os catetos de um triangulo


# V1 de fazer
"""
from math import hypot

# hypot calcula a hipotenusa

a1 = float(input('Digite o cateto adjacente: '))
a2 = float(input('Digite o cateto oposto: '))

print('A hipotenusa é: {}'.format(hypot(a1, a2)))
"""

a1 = float(input('Digite o cateto do triangulo: '))
a2 = float(input('Digite o outro cateto do triangulo: '))

print(f'A hipotenusa é: {(a1**2+a2**2)**(1/2)}')  # Também é possível importar o sqrt para fazer a raiz quadrada
