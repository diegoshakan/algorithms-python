'''Faça um programa que leia um número final e mostre apenas os ímpares'''

fim = int(input('Digite um número fim: '))
cont = 0
while cont <= fim:
    if cont % 2 != 0:
        print(cont)
    cont += 1
