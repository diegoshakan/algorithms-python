'''3.5. Uma empresa concederá um aumento de salário aos seus funcionários, variável de
acordo com o cargo, conforme a tabela abaixo. Crie um algoritmo que leia o salário e o
cargo de um funcionário, calcule e imprima o seu novo salário. Se o cargo do funcionário
não estiver na tabela, informar que o cargo é inválido:
cargo				aumento
prog				50%
analista			40%
DBA				    30%'''

cod = int(input('Digite o número do seu cargo, 1 - Programador, 2 - Analista de Sistemas 3 - Analista de B. Dados: '))
sal = int(input('Qual é o seu salário: '))

if cod == 1:
    print('Seu salário vai aumentar para R$ {}'.format(sal * 0.5 + sal))
elif cod == 2:
    print('Seu salário vai aumentar para R$ {}'.format(sal * 0.4 + sal))
elif cod == 3:
    print('Seu salário vai aumentar para R$ {}'.format(sal * 0.3 + sal))
else:
    print('Código inexistente.')