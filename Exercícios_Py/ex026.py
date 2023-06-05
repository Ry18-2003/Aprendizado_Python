# Ler uma fraze e verificar, quantos "a", primeira e última ocorrência.

a1 = str(input('Fraze favorita: ')).lower().strip()

print(f'A fraze {a1} tem:\n'
      f'Um total de {a1.count("a")} "a".\n'
      f'O primeiro aparece na posição {a1.find("a")+1}.\n'
      f'O último aparece na posição {a1.rfind("a")+1}.')

