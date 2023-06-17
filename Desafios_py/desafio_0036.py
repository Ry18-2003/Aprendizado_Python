# Ler dois valores e falar qual o maior.   

a1 = float(input('Digite um valor: '))
a2 = float(input('Digite um segundo valor: '))

if a1 > a2:
    print(f'Primeiro valor ({a1:.0f}) é maior que o segundo valor ({a2:.0f})')
elif a2 > a1:
    print(f'Segundo valor ({a2:.0f}) é maior que o primeiro ({a1:.0f})')
else:
    print(f'Não ha valor maior.')
