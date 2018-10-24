'''Crie um algoritmo que percorra os 100 primeiros números inteiros e imprima apenas
os pares.'''

cont = 0

while cont <= 100:
    if cont % 2 == 0:
        print(cont)
    cont += 1