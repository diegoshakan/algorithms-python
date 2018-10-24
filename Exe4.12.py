'''4.12. Crie um algoritmo que calcule o fatorial de três números informados pelo usuário.'''

cont = 1
fat = 1
cont2 = 1
fat2 = 1
cont3 = 1
fat3 = 1
num = int(input('Digite o 1º número para fazer o fatorial: '))
num2 = int(input('Digite o 2º número para fazer o fatorial: '))
num3 = int(input('Digite o 3º número para fazer o fatorial: '))
print('-=-=- 1º Fatorial -=-=-')
print(f'Fatorial de {num}:')

for c in range(num):
    fat = cont * fat
    cont += 1
    print(fat, end=' ')
print('\n')
print('-=-=- 2º Fatorial -=-=-')
print(f'Fatorial de {num2}:')
for c in range(num2):
    fat2 = cont2 * fat2
    cont2 += 1
    print(fat2, end=' ')
print('\n')
print('-=-=- 3º Fatorial -=-=-')
print(f'Fatorial de {num3}:')
for c in range(num3):
    fat3 = cont3 * fat3
    cont3 += 1
    print(fat3, end=' ')
print('\n')