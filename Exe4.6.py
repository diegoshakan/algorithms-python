'''Usando uma estrutura de iteração, codifique um algoritmo que leia 8 bits (um a um)
e diga quantos 1s e 0s compõem o byte lido.'''

cont = 1
s0 = 0
s1 = 0

while cont <= 8:
    num = int(input('Digite um bit 1 ou 0: '))
    if num == 0:
        s0 += 1
    else:
        s1 == 1
        s1 += 1
    cont += 1

print(s1)
print(s0)