'''5.11. Construa um algoritmo que leia um número binário entre 00000000 e 11111111 e
calcule o seu valor correspondente na base decimal.'''

numbinario = input('Digite um número binário: ')
numdecimal= int(numbinario, 2)
print(f'{numbinario} em decimal é {numdecimal}.')