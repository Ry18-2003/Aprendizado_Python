# IMC

a1 = float(input('Digite seu peso: '))
a2 = float(input('Digite sua altura: '))

a3 = a1 / a2**2

print(f'Seu IMC é de {a3:.2f}')

if a3 < 18.5:
    print('Você está abaixo do peso')
elif a3 < 25:
    print('Você está na faixa ideal de peso')
elif a3 < 30:
    print('Você está com sobrepeso')
elif a3 < 40:
    print('Você é obeso(a)')
else:
    print('Você tem obsidade morbida, procure um médico')
