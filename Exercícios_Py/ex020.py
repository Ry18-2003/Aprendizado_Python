# sortear uma ordem

from random import sample, shuffle

a1 = str(input('Grupo 1: '))
a2 = str(input('Grupo 2: '))
a3 = str(input('Grupo 3: '))
a4 = str(input('Grupo 4: '))

"""
a5 = [a1, a2, a3, a4]
shuffle(a5)
print(a5)
"""  # Outra forma de fazer

print(f'A ordem de apresentação vai ser: {sample([a1, a2, a3, a4], k=4)}')
