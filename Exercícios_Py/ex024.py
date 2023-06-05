# ler nome de uma cidade e verificar se começa com "Santo"

a1 = str(input('Digite onde você mora: ')).upper().strip()

print(f'A cidade começa com a palavra "Santo"? {"SANTO" in a1[:5]} ')
