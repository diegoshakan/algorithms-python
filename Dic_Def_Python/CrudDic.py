'''
Cadastrar
Remover
Gerar Relatório
Matrícula, Nome dos Alunos e idades
'''

ifrn = {}

def cadastrar(mat, nome, idade):
    ifrn[mat] = [nome, idade]
    print('--- Cadastro efetuado com sucesso! ---\n')

def remover(mat):
    ifrn.pop(mat)
    print(f'--- Matrícula {mat} removido com sucesso. ---\n')

def gerar_relatorio():
    cont = 0
    for chave, valor in sorted(ifrn.items()):
        if valor[1] > 30:
            print(chave, valor)
            cont += 1
    if cont == 0:
        print('--- Ainda não há nenhum aluno matriculado. ---\n')

#Programa Principal

while True:
    print('1. Cadastrar\n2. Remover \n3. Gerar Relatório\n4. Sair:')
    cod = int(input('\nDigite a opção: '))
    print('')
    if cod == 4:
        break
    if cod == 1:
        mat = int(input('Matrícula: '))
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(mat, nome, idade)
    elif cod == 2:
        mat = int(input('Qual matrícula você deseja remover: '))
        remover(mat)
    elif cod == 3:
        gerar_relatorio()