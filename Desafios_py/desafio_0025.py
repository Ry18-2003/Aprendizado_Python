#  Ler o nome completo de uma pessoa e mostrar o primeiro e o último nome

a1 = str(input('Digite o nome completo: '))
a1 = a1.split()

print(f'Primeiro nome: {a1[0]}\nÚltimo nome: {a1[len(a1)-1]}')
