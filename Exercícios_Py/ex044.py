# Preço e condição de pagamento

a1 = float(input('Qual o preço do produto: '))
a2 = str(input('Qual a condição de pagamento: ')).strip().upper()

if a2 == 'CARTÃO' or a2 == 'CARTAO':
    a2 = int(input('Em quantas vezes: '))
    if a2 == 1:
        a1 = a1 * 0.95

    elif a2 >= 3:
        a1 = a1 * 1.2

    print(f'O valor da parcela vai ficar em R${a1/a2:.2f}, totalizando o valor final de R${a1:.2f}')

elif a2 == 'DINHEIRO' or a2 == 'CHEQUE' or a2 == 'PIX':
    a2 = a1 * 0.9
    print(f'O valor final é de R${a2:.2f}')
else:
    print('Forma de pagamento não reconhecida. Tente novamente!')
