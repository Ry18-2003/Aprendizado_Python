# Converção Binario hexa e octal

from cores import letra_amarelo, letra_azul, letra_vermelho, reset

amarelo = letra_amarelo
azul = letra_azul
vermelho = letra_vermelho

a1 = int(input("Escreva um número: "))
a2 = int(input(f"Usar qual base de converção.\n{amarelo}Binaria[0]\n{azul}Octal[1]\n{vermelho}Hexadecimal[2]{reset}\nEscolha: "))

if a2 == 0:

    b2 = ''

    while a1 != 0:
        
        b1 = a1 % 2
        a1 = a1 // 2
        b2 = b2 + str(b1)
        
    print(b2[::-1])  # Comando bin pode ser usado para substituir essa parte matematica

elif a2 == 1:
    print(oct(a1[2:]))

elif a2 == 2:
    print(hex(a1[2:]))

else:
    print("Nenhum valor valido selecionado. Tenha um bom dia.")
