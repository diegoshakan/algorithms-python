#3.1. Crie um algoritmo que leia 2 números e informe o maior deles.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

maior = a

if maior < b:
    maior = b

print(maior)