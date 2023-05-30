a1 = str(input('Escreva algo: '))

print(f'A classe: {type(a1)}\nSó tem espaços: {a1.isspace()}\nSó tem números: {a1.isnumeric()}\n'
      f'Só tem letras: {a1.isalpha()}\nA letra e ou números: {a1.isalnum()}\n'
      f'Está somente em maiúsculas: {a1.isupper()}\nEstá somente em minúsculas: {a1.islower()}\n'
      f'Está capitalizada: {a1.istitle()}')
