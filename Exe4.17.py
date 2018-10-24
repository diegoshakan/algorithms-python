'''4.17. Construa uma aplicação para receber o nome e o preço de uma quantidade
indeterminada de produtos. Cada vez que o usuário informar esses dados, o sistema deve
perguntar se ele deseja continuar (a aplicação só deverá ser encerrada quando o usuário
informar “N”). Ao fim, o sistema deve informar o nome e o preço do produto mais caro.'''

continuar = ''
prodmaior = 0


while continuar.upper() != 'N':
    nome = input('Nome do produto: ')
    preco = float(input('Valor do produto: '))
    if preco > prodmaior:
        prodmaior = preco
        nome = nome
    continuar = input('Deseja continuar a inserir dados [S/N]: ')
print(f'O produto {nome} é o mais caro e custa R$ {prodmaior:.2f}')