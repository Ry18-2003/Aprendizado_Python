# Manipulação de cadeias de texto

a1 = 'Richard Chrisperi Martins'
print(a1[6])
print(a1[2: 6])
print(a1[1:7:2])
print(a1[:3], a1[1:], a1[::2], a1[1::2])
a2 = a1.split()
print(len(a1))

print(a1.split(), ''.join(a1[0::5],))

a2 = ''.join(a2)
print(len(a2))
print('Quantos letras "r" dentro da variável: ', a1.lower().count('r'),
      '. Quantas letras "r" a partir da posição 1: ', a1.lower().count('r', 1, 7),
      '. A posição de inicio de "char": ', a1.find('char'))

print('ard' in a1)
