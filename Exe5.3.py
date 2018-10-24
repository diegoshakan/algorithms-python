'''5.3. Crie um vetor que leia e armazene 10 números inteiros positivos distintos informados
pelo usuário (os números variam entre 1 e 300). Em seguida, mostre na tela o menor e o
maior número informado e em qual posição eles se encontram.'''

cont = 0
lista = []

while cont < 10:
    num = int(input(f'Digite um número para inserir na lista: '))
    cont += 1
    lista.append(num)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'O menor número é {min(lista)}.')
print(f'E está na posição {lista.index(min(lista))} do vetor.')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'O maior número é {max(lista)}.')
print(f'E está na posição {lista.index(max(lista))} do vetor.')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')