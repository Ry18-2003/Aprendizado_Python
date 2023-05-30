#  Verificações do tipo str

a1 = str(input('Digite algo: '))

print(f'A classe é: {type(a1)}\nContém apenas número: {a1.isnumeric()}\nContém apenas letras: {a1.isalpha()}\n'
      f'Contém apenas espaços: {a1.isspace()}\nContém letras e ou números sem espaços: {a1.isalnum()}\n'
      f'É exibível na tela: {a1.isprintable()}\n'
      f'Contém apenas caracteres American Standard Code for Information Interchange: {a1.isascii()}\n'
      f'Contém apenas números decimais: {a1.isdecimal()}\nContém apenas dígitos: {a1.isdigit()}\n'
      f'É um nome de variável valido: {a1.isidentifier()}\nEstá em apenas minúsculas: {a1.islower()}\n'
      f'Está em apenas maiúsculas{a1.isupper()}\n'
      f'As palavras começam com letras maiúsculas e as demais são minúsculas: {a1.istitle()}')
