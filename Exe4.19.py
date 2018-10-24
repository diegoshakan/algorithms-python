'''4.19. Construa um algoritmo que leia uma quantidade indeterminada de números e
escreva quantos deles estão no intervalo [1, 50] (incluindo os valores 1 e 50 no intervalo)
e quantos estão fora. Para que o programa seja encerrado, o usuário deve responder à
pergunta se deseja (ou não) continuar a informar números.'''

continuar = ''
cont = 0
cont2 = 0

while continuar.upper() != 'N':
    num = int(input('Digite um número: '))
    if num > 0 and num < 51:
        cont += 1
    else:
        cont2 += 1
    continuar = input('Deseja continuar [S/N]: ')
print(f'{cont} número(s) estão no intervalo de 1 a 50, e {cont2} número(s) não estão neste intervalo.')