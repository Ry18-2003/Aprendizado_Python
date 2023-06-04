# Ler quantas vezes a letra "a" aparece, qual a posição que aparece primeiro, e qual posição aparece por último

a1 = str(input('Digite uma fraze: '))

print(f'Sua fraze tem {a1.lower().count("a")} "a"\nO primeiro está na posição {a1.lower().find("a")}.\n'
      f'O último está ná posição {a1.lower().rfind("a")}')

