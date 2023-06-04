# Ler um nome, e ver se tem "Silva" em qualquer parte do nome

a1 = str(input('Nome: '))

print(f'Há o sobrenome "Silva" nesse nome: {"SILVA" in a1.upper()}')