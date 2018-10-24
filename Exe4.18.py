'''4.18. Construa um algoritmo que leia 5 números e escreva quantos deles estão no
intervalo [10, 20] (incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora.'''

cont = 0
cont2 = 0

for c in range(5):
    num = int(input('Digite um número: '))
    if num > 9 and num < 21:
        cont += 1
    else:
        cont2 += 1
print(f'{cont} número(s) estão no intervalo de 10 a 20, e {cont2} número(s) não estão neste intervalo.')