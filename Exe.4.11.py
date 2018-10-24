'''4.11. Crie um algoritmo que calcule o fatorial de um número informado pelo usuário.'''

cont = 1
fat = 1
num = int(input('Digite o número para fazer o fatorial: '))
for c in range(1, num+1):
    fat = cont * fat
    cont += 1
    print(fat, end=' ')