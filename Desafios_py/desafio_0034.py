# Financiamento de casa
import cores

titulo = cores.letra_vermelho
bordas = cores.letra_amarelo

print(f'{bordas}{"="*30}\n{titulo}{"Financiamento de casa":^30}\n{bordas}{"="*30}{cores.reset}')


a1 = float(input('Valor da casa a financiar: '))
a2 = float(input('Digite seu salário: '))
a3 = int(input("Enquantos anos pretende financiar: "))

if a1 / (a3 * 12) > a2 * 0.3:
    print(f'{titulo}Financiamento negado. {cores.reset}Tenha um bom dia.')
else:
    print(f'{cores.letra_verde}Seu financimento foi aprovado. {cores.reset}Tenha um bom dia.')
