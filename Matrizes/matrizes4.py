'''Crie e teste uma função que receba, como argumento, uma matriz M. Ao fim, a função deve
retornar uma string informando se M é uma matriz esparsa.'''

def matriz_esparsa(matriz, linha, coluna):
    ex = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] != 0:
                ex -= 1
            else:
                ex += 1
    return ex

#Principal

matriz_global = []
linha_global = int(input('Linhas: '))
coluna_global = int(input('Colunas: '))

for i in range(linha_global):
    A = []
    for j in range(coluna_global):
        A.append(int(input(f'Valor da posição {i} X {j}: ')))
    matriz_global.append(A)

recebe = matriz_esparsa(matriz_global, linha_global, coluna_global)
if recebe > 0:
    print('Esparsa')
else:
    print('Não Esparsa')