'''Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer 
no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 
casas decimais após a vírgula, segundo a fórmula:
Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois 
valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto 
flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, 
com 4 casas após o ponto decimal.
'''
from math import sqrt
# entradaX = input().split(' ')
# entradaY = input().split(' ')
# x1, x2 = entradaX
# y1, y2 = entradaY
# distancia  = sqrt (((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2))
# print('{:.4f}'.format(distancia))

entrada1 = input().split(' ')
entrada2 = input().split(' ')
x1,y1 = entrada1
x2,y2 = entrada2
distancia = sqrt((float(x2) - float(x1))**2 + (float(y2)-float(y1))**2)
print("{:.4f}".format(distancia))