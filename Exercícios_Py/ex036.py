# Emprestimo

a1 = float(input('Valor da casa: '))
if a1 > 0:
    a2 = float(input('Seu salário: '))
    a3 = int(input('Em quanto anos pretende pagar: '))

    if not a1 / (a3 * 12) > a2 * 0.30 and a3 != 0:
        print('Emprestimo aprovado!')
    else:
        print('Emprestimo recusado!')

else:
    print('Valor invalido!')

