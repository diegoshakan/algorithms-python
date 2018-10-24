'''4.21. Construa um algoritmo que leia uma quantidade indeterminada de números
positivos. Quando o usuário informar um valor negativo, a aplicação deve ser encerrada.
Ao fim, imprima a média aritmética dos valores positivos lidos.'''

cont = 0
num = 0
soma = 0

while num >= 0:
    num = int(input('Digite um número, apenas positivo: '))
    if num >= 0:
        soma += num
        cont += 1

print(f'A média aritmética dos números positivos foi {soma / cont}')