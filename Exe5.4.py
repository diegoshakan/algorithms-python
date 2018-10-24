'''5.4. Crie um vetor A que leia e armazene 10 números. Crie um vetor B que leia e
armazene outros 10 números. Em seguida, permute os valores entre os vetores.'''

a = []
b = []
c = []
cont = 0

while cont < 3:
    numa = int(input('Digite um número para inserir na lista A: '))
    a.append(numa)
    numb = int(input('Digite um número para inserir na lista B: '))
    b.append(numb)
    cont += 1
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Abaixo estão as listas antes da permuta:')
print(f'Lista A {a}')
print(f'Lista B {b}')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Abaixo estão as listas depois da permuta:')

c = a
a = b
b = c

print(f'Lista A {a}')
print(f'Lista B {b}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')