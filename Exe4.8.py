'''Usando loop , crie um algoritmo para ler 5 idades e calcular a média aritmética entre
elas.'''

cont = 0
soma = 0

while cont < 5:
    idade = int(input('Digite uma idade: '))
    soma = soma + idade
    cont += 1

print('A média aritimética das idades é: {} anos'.format(soma / cont))