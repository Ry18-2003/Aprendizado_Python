# verificar o IMC

print(f'{"=-"*20}=\n{"Calculadora de IMC":^41}\n{"=-"*20}=\n')

a1 = str(input('Peso: '))
a1 = float(a1.replace(',', '.'))

a2 = str(input('Altura: '))
a2 = int(a2.replace('.', '').replace(',', ''))

a3 = float(f"{(a1)/(a2/100)**2:.2f}")

if a3 < 18.5:
    print(f'Você está abaixo do peso, com o IMC de {a3} kg/m²')
elif a3 < 25:
    print(f'Você está no peso normal. Seu IMC é de {a3} kg/m²')
elif a3 < 30:
    print(f'Você está com sobrepeso e seu IMC é de {a3} kg/m²')
elif a3 < 40:
    print(f'Você está com obesidade e seu IMC é de {a3} kg/m²')
else:
    print(f'Você está em obesidade mórbida. IMC de {a3} kg/m²')
