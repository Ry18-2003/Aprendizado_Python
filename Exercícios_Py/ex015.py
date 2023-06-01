# aluguel de carro, dia R$60 km R$0,15

a1 = int(input('Quantos dias: '))
a2 = int(input('Quantos km: '))

print(f'Por ter rodado por {a1} dias, e andado por {a2}km, o preço do aluguel é R${a1*60+a2*0.15:.2f}')
