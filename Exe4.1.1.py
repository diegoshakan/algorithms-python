'''Faça um programa que leia um número final e mostre apenas os pares'''

fim = int(input('Digite um número final: '))
cont = 0
while cont <= fim:
    if cont % 2 == 0:
        print(cont)
    cont += 1
