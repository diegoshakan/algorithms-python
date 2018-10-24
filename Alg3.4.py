#3.4. Crie um algoritmo que leia 1 número e indique se ele é par ou ímpar.

a = int(input('Digite um número:'))

res = a % 2

if res != 0:
    print('Ímpar')
else:
    print('Par')