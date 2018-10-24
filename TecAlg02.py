'''QUESTÃO 02. Crie uma aplicação na qual o usuário informe a idade de um número indeterminado de
atletas do IFRN a fim de categorizá-los, conforme tabela abaixo. Para encerrar a leitura dos dados,
defina uma condição de parada. Ao fim, o programa deve gerar um relatório indicando o percentual de
atletas por categoria.

Infantil    Entre 11 e 15 anos
Juvenil     Entre 16 e 17 anos
Adulto      A partir dos 18 anos'''

sair = ''
cont = 0
inf = 0
juv = 0
ad = 0
while sair.upper() != 'S':
    idade = int(input('Idade: '))
    if idade >= 11 and idade <= 15:
        inf += 1
    elif idade > 15 and idade <= 17:
        juv += 1
    elif idade >17:
        ad += 1
    cont += 1
    infantil = (inf * 100) / cont
    juvenil = (juv * 100) / cont
    adulto = (ad * 100) / cont
    sair = input('Sair? [S/N]: ')
print(f'Atletas categoria Infantil são {infantil}%')
print(f'Atletas categoria Juvenil são {juvenil}%')
print(f'Atletas categoria Adulto são {adulto}%')
