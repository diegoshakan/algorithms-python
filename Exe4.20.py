'''4.20. Construa um programa que leia 10 valores no intervalo [1, 1000] e, ao fim, escreva
o maior e o menor valor lido.'''

lista = []

for c in range(3):
    num = int(input('Digite um número entre 1 e 1000: '))
    if num >= 1 and num <= 1000:
        lista.append(num)
    else:
        print('Somente números entre 1 e 1000 serão computados.')
        break
print(f'O maior valor lido foi {max(lista)}')
print(f'O menor valor lido foi {min(lista)}')