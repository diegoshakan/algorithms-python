'''Escreva um programa que leia três valores com ponto flutuante de dupla precisão: 
A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das 
áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois 
pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto 
decimal.
'''
entradas = input().split(' ')
A, B, C = entradas
tri = (int(A) * int(C))/2
circ = 3.14159 * int(C) ** 2
trap = ((int(A) + int(B)) * int(C))/2
quad = int(B)**2
retan = int(A) * int(B)
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(tri, circ, trap, quad, retan))