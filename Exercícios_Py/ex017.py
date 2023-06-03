# Digitar catetos e mostrar a hipotenusa
"""
from math import hypot

a1 = float(input('Digite o cateto oposto: '))
a2 = float(input('Digite o cateto adjacente: '))
a3 = hypot(a1, a2)

print(f'A hipotenusa dos catetos {a1} e {a2} é {a3:.2f}')
"""  # Resolução importando biblioteca


a1 = float(input('Digite um cateto do triangulo: '))
a2 = float(input('Digite o outro cateto: '))

print(f'A hipotenusa dos catetos {a1} e {a2} é {(a1**2+a2**2)**(1/2):.2f}')
