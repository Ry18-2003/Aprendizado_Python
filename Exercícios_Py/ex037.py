# converçor

a1 = int(input('Escolha [1-Binario] [2-Hexadecimal] [3-Octal]\n:'))
if a1 == 1:
    a1 = int(input('Digite o número para converção em BINARIO: '))
    print(f'O número {a1} convertido para Binario é: {bin(a1)[2:]}')

elif a1 == 2:
    a1 = int(input('Digite o número para converção em HEXADECIMAL: '))
    print(f'O número {a1} convertido para HEXADECIMAL é: {hex(a1)[2:]}')

elif a1 == 3:
    a1 = int(input('Digite o número para converção em OCTAL: '))
    print(f'O número {a1} convertido para octal é: {oct(a1)[2:]}')
else:
    print('Valor invalido!')
