'''5.10. Crie um algoritmo que apresente a série de Fibonacci até o 20° termo. A série
numérica é a seguinte: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, ...'''

ant, pos = 1, 0
print(0, end=' ')
for c in range(1, 20):
    prox = pos + ant
    ant = pos
    pos = prox
    print(prox, end=' ')