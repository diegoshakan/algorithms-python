'''2-  Crie  um  programa  que,  usando  dicionário,  represente  uma  agenda  de  tamanho  fornecido
inicialmente pelo usuário. Leia os dados de todos os contatos do usuário de forma que a agenda fique
completa e por fim imprima todos os contatos.'''

qnt = int(input('Quantos contatos: '))
agenda = {}

for i in range(qnt):
    nome = input('Digite nome: ')
    telefone = input('Digite número: ')
    agenda[nome] = telefone


for chave in sorted(agenda):
    print(f'{chave}: {agenda[chave]}')