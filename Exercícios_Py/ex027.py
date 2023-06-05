# Ler um nome completo, e mostrar o primeiro e o último nome.

a1 = str(input('Digite seu nome completo: ')).title().strip().split()
print(f'Curioso.\n'
      f'Seu primeiro nome é {a1[0]}\n'
      f'E seu último nome é {a1[-1]}')
