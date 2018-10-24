import locale
from math import sqrt

'''2.6 Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no plano, 
P(x1,y1) e P(x2,y2), escreva a distância entre eles. A fórmula que efetua tal cálculo é: 
d=raiz quadrada de ->(x2-X1)^2 + (y2-y1)^2'''


x1 = float(input("X1: "))
y1 = float(input("Y1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))


d = sqrt(((x2-x1)**2) + ((y2-y1)**2)) #sqrt é uma função matemática que precisa ser importada.
print(locale.format("%.4f", d)) #locale.format tb precisa ser importada para que a formatação aconteça.