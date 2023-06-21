# Pagamento, acrecimo e decrecimo de valores

a1 = float(input('Insira o valor da compra: '))
if a1 > 0:
    a2 = str(input('Forma de pagamento [1/dinheiro/cheque] [2/Cartão]: ')).lower().strip()

    if a2 == '1' or a2 == 'dinheiro' or a2 == 'cheque' or a2 == '2' or a2 == 'cartão' or a2 == 'cartao':

        if a2 == '2' or a2 == 'cartão' or a2 == 'cartao':
            a2 = int(input('Você selecionou o modo de pagamento 2, Cartão. Desaja parcelar em quantas vezes: '))
        
            if a2 >= 3:
                print(f'A compra no valor de R${a1:.2f} vai ter suas parcelas no valor de R${(a1*1.20)/a2:.2f}. Totalizando um total de {a1*1.20:.2f}\n'
                    f'Tenha um bom dia!!!')
            
            elif a2 == 2:
                print(f'A compra vai sair por R${a1:.2f}\nTenha um bom dia!!!')
            
            elif a2 == 1:
                print(f'A compra no valor de R${a1:.2f} vai sair no valor de R${a1*0.95:.2f}\nTenha um bom dia!!!')
            
            else:
                print('Número de parcelas invalidas')

        elif a2 == '1' or a2 == 'dinheiro' or a2 == 'cheque':
            print(f'Metodo de pagamento em dinheiro ou cheque selecionado.\nA compra no valor de R${a1:.2f} vai sair no valor de R${a1*0.90:.2f}\n'
                   'Tenha um bom dia!!!')

    else:
        ('Forma de pagamento invalida. Tenta novamente.')

else:
    print('Valor invalido. Tente novamente.')
