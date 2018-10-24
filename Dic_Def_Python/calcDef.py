'''
cadastrar
remover
gerar relatório

matricula, nome e idade
'''

alunos = {2: ['diego', 33], 1: ['kassandra', 34], 3: ['Aimée', 4]}

def cadastrar(mat, nome, idade):
    alunos[mat] = [nome, idade]
    print('Cadastro Realizado com sucesso.')

def remover(mat):
    alunos.pop(mat)
    print('Removido com sucesso.')

while True:
    print('1. Cadastrar\n2. Remover\n3. Gerar Relatório\n4. Sair')
    cod = int(input('Opção: '))
    if cod == 1:
       mat = int(input('Matrícula: '))
       nome = input('Nome: ')
       idade = int(input('Idade: '))
       cadastrar(mat, nome, idade)
    elif cod == 2:
        mat = int(input('Qual matrícula você deseja remover: '))
        remover(mat)
    elif cod == 3:
        for chave, valor in sorted(alunos.items()):
            if valor[1] > 30:
                print(chave, valor)
    elif cod == 4:
        print('Até mais!')
        break