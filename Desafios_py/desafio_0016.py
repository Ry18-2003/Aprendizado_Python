# Ler um angulo e mostrar o seno, o cosseno e o tangente

from math import cos, tan, sin, radians

# cos. mostra o cosseno, tan. exibe o tangente, sin. é o seno e radians transforma o valor em radianos, pois
# cos., tan. e sin. esperam valores em radiano

a1 = float(input('Digite um ângulo: '))

print('O seno é {:.2f}, o cosseno é {:.2f} e o tangente é {:.2f}'
      ''.format(sin(radians(a1)), cos(radians(a1)), tan(radians(a1))))


# revisar depois
