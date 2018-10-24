'''Crie e teste uma função que receba, como argumento, uma matriz quadrada M. Ao fim, a
função deve retornar uma string informando se M é uma matriz nula.'''


def nula(matriz, linha, coluna):
    x = True
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] != 0:
                x = False
                break
    return x

#Principal

matriz_global = []
linha_global = int(input('Linhas: '))
coluna_global = int(input('Colunas: '))

for i in range(linha_global):
    A = []
    for j in range(coluna_global):
         A.append(int(input(f'Valor da posição {i} X {j}: ')))
    matriz_global.append(A)

recebe = nula(matriz_global, linha_global, coluna_global)
if recebe == True:
    print('Nula')
else:
    print('Nula')