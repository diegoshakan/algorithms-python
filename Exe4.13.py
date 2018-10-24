'''4.13. A prefeitura de João Câmara contratou uma software house para desenvolver um
sistema para coleta de informações dos seus habitantes. Os dados a serem pesquisados
são SALARIO e NUMERO DE FILHOS de cada habitante. O sistema só deverá ser
encerrado quando o usuário informar que não deseja mais realizar a pesquisa. Ao fim, o
sistema deve gerar o seguinte relatório:
• Número de pessoas pesquisadas;
• Média de salário da população;
• Média do número de filhos;
• Percentual de pessoas com salário menor que R$ 400,00.
• Maior salário.'''

cont = 0
contsal = 0
somafilhos = 0
somasalario = 0
maiorsalario = []
pesquisa = ''

while pesquisa in 'Ss':
    salario = float(input('Qual é o seu salário: '))
    maiorsalario.append(salario) # acrescenta os salários em uma lista
    somasalario += salario # soma os salários para fazer a média no final
    if salario < 400: # para verificar os que recebem menos que o valor pedido
        contsal += 1 # conta os que recebem menos, para fazer o cálculo da porcentagem
    filhos = int(input('Quantos filhos você tem: '))
    somafilhos += filhos # soma número de filhos para fazer a média no final
    cont += 1 #contador de quantas vezes o programa irá rodar fazendo as pesquisas com as pessoas.
    pesquisa = input('Deseja continuar a pesquisa [S/N]: ') # para fazer a verificação se vai continuar a pesquisa.
    if pesquisa.upper() == 'N':
        break
mediasalario = somasalario / cont
mediafilhos = somafilhos / cont
por = (contsal * 100) / cont
print(f'{cont} pessoas realizaram a pesquisa.')
print(f'A média salarial dos entrevistados é R$ {mediasalario:.2f}')
print(f'A média de filhos dos entrevistados é {mediafilhos:.2f}')
print(f'A porcentagem de pessoas que recebem menos que R$ 400,00 é {por:.2f}%' ) # Transforma em porcentagem
print(f'O maior salário é R$ {max(maiorsalario):.2f}.')