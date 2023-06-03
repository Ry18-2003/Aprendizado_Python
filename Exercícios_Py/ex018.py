# calculo de seno, cosseno e tangente

from math import radians, sin, cos, tan

a1 = float(input('Digite um ângulo: '))
a2 = radians(a1)

print(f'Do ângulo {a1}, temos o seno {sin(a2):.2f} e cosseno {cos(a2):.2f} e o tangente {tan(a2):.2f}.'
      f' O radiano é {a2:.2f}')
