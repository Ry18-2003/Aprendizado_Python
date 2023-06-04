# Ler um nome de cidade e dizer se começa ou não com a palavra "SANTO"

a1 = str(input('Nome: '))
a1 = a1.split()
print(f'Começa com a palavra "SANTO": {"SANTO" in a1[0].upper()}')
