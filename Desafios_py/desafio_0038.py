# Ler media, e indicar reprovado, recuperação e aprovado

from cores import letra_amarelo, letra_vermelho, letra_verde, reset

a1 = float(input('1° Nota: '))
a2 = float(input('2° Nota: '))

if (a1 + a2) / 2 <= 4.9:
    print(f'{letra_vermelho}Reprovado!{reset} com média de:{letra_vermelho} {(a1+a2)/2}')
elif (a1 + a2) / 2 <= 6.9:
    print(f'{letra_amarelo}Recuperação!{reset} com média de:{letra_amarelo} {(a1+a2)/2}')
else:
    print(letra_verde, f'Aprovado!{reset} com a média de:{letra_verde} {(a1+a2)/2}')
