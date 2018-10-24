'''5.5. Leia um vetor A de 10 números inteiros. Em seguida, leia um número digitado pelo
usuário e armazene-o na variável num. Multiplique cada elemento de A pela variável num
e armazene os resultados em um vetor B. Em seguida, imprima o vetor B.'''

listaA = []
listaB = []
num = int(input('Digite um número para multiplicar por cada elemento da listaA: '))

for c in range(10):
    a = int(input('Digite um número para acrescentar na listaA: '))
    listaA.append(a)
    listaB.append(a*num)

print(listaB)

