'''Dados 10 números digitados pelo usuário, construa um algoritmo para mostrar a
média apenas dos números menores que zero.'''

cont = 0
soma = 0
menor = 0

while cont < 10:
    num = int(input('Digite um número: '))#Recebe um número, acontecerá 10 vezes
    if num < 0: #se o número for menor que zero ele entra em um contador
        menor = menor + 1 #este é o contador para saber qnts números negativos existem.
        soma = soma + num #vai somar apenas os números negativos para fazer sua média.
    cont = cont + 1 #contador para dar fim ao processo
print(soma / menor) #soma dos números negativos, dividido pelas vezes que

