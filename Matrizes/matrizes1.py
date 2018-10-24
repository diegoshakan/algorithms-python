'''Crie um programa que solicite ao usuário uma quantidade N de itens de uma lista, onde N
deve ser ímpar e maior que 1. Em seguida, o programa principal deve invocar uma função chamada
carrega_lista, que receba como argumento N; esta função deve retornar uma lista L para o programa
principal. Após receber L, o programa principal deve passá-la como parâmetro para uma função chamada
retorna_elemento_central_lista. Após receber o elemento central da lista, o programa principal deve enviar
esse elemento para outra função chamada calcula_fatorial, a qual devolverá o fatorial de um número
passado como parâmetro. Por fim, o programa principal deve escrever o fatorial do elemento central da
lista.'''

def cria_lista(a):
    e = 3
    L = []
    for i in range(a):
        L.append(int(input('Digite um valor: ')))
    return L

def centro_lista(a, b):
    p = a / 2
    num_central = b[int(p)]
    return num_central



def faz_fatorial(c):
    F = 1
    for i in range(1, c + 1):
        F = F * i
    return F

while True:
    print('1. Digite um número ímpar e maior que 1, será quantidade de valores dentro da lista.\nOu 0 Para sair: ')
    num = int(input(''))
    if num % 2 != 0 and num > 1:
        X = cria_lista(num)
        Y = centro_lista(num, X)
        Z = faz_fatorial(Y)
        print()
        print(f'O fatorial de {Y} é {Z}')
        print()
    elif num == 0:
        break