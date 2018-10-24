'''4.15. Construa um algoritmo para receber o código e preço de 5 produtos. Ao fim da
leitura dos produtos, informar o código do produto mais caro, o seu valor, bem como a
média aritmética dos preços lidos.'''

precomaior = 0
soma = 0
cont = 0

for c in range(3):
    cod = int(input('Código do Produto: '))
    preco = float(input('Preço do Produto: '))
    if preco > precomaior:
        precomaior = preco
        cod = cod
    soma += preco
    cont += 1
print(f'O maior preço é R$ {precomaior:.2f} e seu código é {cod}.')
print(f'A média dos valores são R$ {soma / cont:.2f}')