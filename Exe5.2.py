'''5.2. Crie um vetor de 10 posições do tipo real e insira valores nele. Em seguida, verifique
se há números menores que zero. Se sim, troque o seu conteúdo por 1 e, ao fim, imprima
o novo vetor.'''

lista = []
cont = 0

while cont < 10:
    num = float(input('Digite um número: '))
    cont += 1
    if num < 0:
        num = 1.0
    lista.append(num)
print(lista)

