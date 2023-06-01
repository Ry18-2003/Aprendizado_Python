# conversor de medida

a1 = float(input('Digite uma medida: '))
print(f'{a1}m é igual a:\nkm: {a1/1000}km\nhm: {a1/100}hm\ndam: {a1/10}dam\n'
      f'dm: {a1*10:.0f}dm\ncm: {a1*100:.0f}cm\nmm: {a1*1000:.0f}mm')
