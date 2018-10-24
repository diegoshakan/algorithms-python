'''2.7. Escreva um algoritmo que leia três números inteiros e positivos (A, B, C), calcule o
valor de D  e imprima D, onde:
d = (r+s)/2 onde r= (a+b)² e S=(b+c)²'''


a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

r = (a + b)**2
s = (b + c)**2

if a < 0 or b < 0 or c < 0:
    print("Somente números positivos")
else:
    d = (r + s) / 2
    print(d)
