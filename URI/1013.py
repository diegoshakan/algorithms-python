'''Faça um programa que leia três valores e apresente o maior dos três valores lidos 
seguido da mensagem “eh o maior”. Utilize a fórmula:

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
entrada = input().split(' ')
a, b, c = entrada
maiorAB = (int(a) + int(b) + abs(int(a)-int(b)))/2
maiorTotal = (int(maiorAB) + int(c) + abs(int(maiorAB) - int(c)))/2
print('{} eh o maior'.format(int(maiorTotal)))