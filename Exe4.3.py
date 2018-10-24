'''4.3. Crie um algoritmo que calcule a soma dos 50 primeiros números inteiros positivos e
mostre o resultado da soma.'''

n = 1
soma = 0
x = 0
while n <= 50:
    x = x + 1
    soma = soma + x
    n = n + 1
    print(soma)