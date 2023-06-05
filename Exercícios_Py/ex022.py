# Mostra um nome digitado: Maiúsculo, Minúsculo, quantas letras tem no nome, desconsiderando espaços
# e quantas letras tem o primeiro nome.

a1 = str(input('What is your name: ').strip())
a2 = a1.split()

print(f'Analyzing your name...\nYour name in upper letters: {a1.upper()}\nYour name in lower letters: {a1.lower()}')

# a1 = "".join(a2)

# print(f'Your name has {len(a1)} letters.\nAnd your first name has {len(a2[0])} letters.')

print(f'Your name has {len(a1) - a1.count(" ")} letters.\nAnd your first name has {a1.find(" ")} letters.')