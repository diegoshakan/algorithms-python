'''5.7. Leia um vetor de 10 posições e, em seguida, leia dois valores X e Y quaisquer
correspondentes a duas posições no vetor. Ao fim, o programa deve escrever a soma dos
valores encontrados nas respectivas posições X e Y.'''

lista = []
x = int(input('Digite uma posição no vetor entre 0 e 9: '))
y = int(input('Digite uma outr posição no vetor entre 0 e 9: '))

for c in range(3):
    a = int(input('Insira um valor na lista: '))
    lista.append(a)
soma = lista[x] + lista[y]
print(f'A soma dos números na posição x = {lista[x]} e y = {lista[y]} é = {soma}')