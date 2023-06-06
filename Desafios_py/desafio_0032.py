# ler o salário de um funcionário e fazer um acréscimo de 10% para salário acima de R$1250.00 e de 15% para salários abaixo.

a1 = int(input('Informe o salário: '))

print(f"O salário vai passar a ser R${a1 * 1.15 if a1 <= 1250 else a1 * 1.10:.2f}.")
print(f'Tendo recebido {"15%" if a1 <= 1250 else "10%"} de aumento.')
