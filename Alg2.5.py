'''2.5.  Escreva  um  algoritmo  que  leia  2  valores,  insira os  em duas
variáveis  e  permute os valores entre elas. Ao fim, imprima o valor das variáveis
antes e depois da permutação.'''


a = int(input("Número 1: "))
b = int(input("Número 2: "))

print(a, b)

aux = a
a = b
b = aux

print(a, b)
