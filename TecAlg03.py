'''QUESTÃO  03. Crie  uma  aplicação  na  qual  o  usuário  informe o  código  do  cargo  de  um
funcionário  (ver  tabela abaixo) e  o  seu  respectivo  salário.
Para  encerrar  a leitura  dos  dados, defina uma  condição de  parada. Ao fim,  o programa deve
informar a média salarial dos nutricionistas.
1   Enfermeiro
2   Nutricionista
3   Médico
'''

cont = 0
soma = 0
sair = ''
while sair != 'N':
    cod = int(input('''Qual o código:
1 - Enfermeiro: 
2 - Nutricionista: 
3 - Médico: 
0 - Sair
Selecione: '''))
    if cod == 1:
        enf = float(input('Salário do Enfermeiro: '))
    elif cod == 2:
        nut = float(input('Salário do Nutricionista: '))
        soma += nut
        cont += 1
        media = soma / cont
    elif cod == 3:
        med = float(input('Salário do Médico: '))
    elif cod == 0:
        break
    else:
        print('Código não existe.')
print(f'A média salarial, dos nutricionistas, é de R$ {media:.2f}')