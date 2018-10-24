'''Crie e teste uma função que receba uma matriz quadrada. Ao fim, ela deve retornar uma
string informando se a matriz é identidade'''

def matriz(a, b):
    m = []
    for i in range(a):
        x = []
        for j in range(b):
            x.append(float(input(f'Digite o elemento da posição {i}x{j} ')))
        m.append(x)
    a = True
    for i in range(a):
        for j in range(b):
            if i == j:
                if m[i][j] != 1:
                    a = False
                    break
            else:
                if m[i][j] != 0:
                    a = False
                    break
    return a

#Programa Principal

while True:
    print()
    print('--- Insira uma matriz de mesmo números de linhas e colunas ---')
    print()

    linhas = int(input('Linhas: '))
    colunas = int(input('Colunas: '))

    if linhas == colunas:
        mat = matriz(linhas, colunas)
        if mat == True:
            print('Identidade')
        else:
            print('Não é identidade')

    print()