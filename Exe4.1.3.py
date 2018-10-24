'''Faça um programa que some dez números'''

cont = 0
soma = 0

while cont < 10:
    num = int(input('Leia um número: '))
    soma = soma + num
    cont = cont + 1

print(soma)