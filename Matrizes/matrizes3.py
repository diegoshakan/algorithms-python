'''Crie e teste uma função que receba dois argumentos: uma constante k e uma matriz A. Ao
fim, a função deve retornar o resultado da operação k * A.'''

def multiplicar(k, A):
    return (k * A)

def matriz(a, b):
    m = []
    for i in range(a):
        x = []
        for j in range(b):
            x.append(float(input(f'Digite o elemento da posição {i}x{j} ')))
        m.append(x)
        if m[i][j] > len(m[i][j]):
            break
    return m

k = int(input('insira um valor para constante: '))

while True:
    linhas = int(input(''))
    colunas = int(input(''))
    matriz(linhas, colunas)
    m = matriz(linhas, colunas)

print(multiplicar(k, m))