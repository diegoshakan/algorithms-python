'''5.9. Escreva um algoritmo que leia um vetor de 10 posições e mostre-o. Em seguida,
troque o primeiro elemento com o último, o segundo com o penúltimo, o terceiro com o
antepenúltimo, e assim sucessivamente. Mostre o novo vetor depois da troca.'''

listaa = []

for c in range(10):
    num = int(input('Digite um número: '))
    listaa.append(num)

print(listaa)
print(listaa[::-1])
