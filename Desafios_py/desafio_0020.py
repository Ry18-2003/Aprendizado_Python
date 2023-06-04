# Manipular strings, nome completo.
# Maiúscula, minúscula, quantas letras desconsiderando espaços e quantas letras a primeira parte

a1 = str(input('Nome completo: '))
a2 = a1.split()
a3 = ''.join(a2)
print(f'Nome em maiúsculo: {a1.upper()}\nNome em minúsculo: {a1.lower()}\n'
      f'Número de letras, desconsiderando espaços: {len(a3)}\nQuantas letras tem o primeiro nome: {len(a2[0])}')