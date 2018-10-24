'''5.8. Leia dois vetores, A e B, de 10 posições. Gere um vetor C contendo, nas posições
pares os valores de A e nas posições impares os de B.'''

listaA = []
listaB = []
listaC = []


for c in range(10):
    a = int(input('Insira um número para listaA: '))
    listaA.append(a)
    listaC.append(a)
    b = int(input('Insira um número para listaB: '))
    listaB.append(b)
    listaC.append(b)

print(listaA)
print(listaB)
print(listaC)