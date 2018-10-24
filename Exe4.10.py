'''4.10. Em uma sala com 15 alunos, são informados o sexo e idade de cada um. Construa
um algoritmo para verificar quantos são do sexo feminino e do masculino. Informe
também quantos são maiores de 18 anos.'''

contm = 0
contf = 0
cont = 0

for c in range(15):
    sexo = input('Qual é o sexo [M/F]: ')
    idade = int(input('Sua idade: '))
    if sexo in 'Mm':
        contm += 1
    elif sexo in 'Ff':
        contf += 1
    if idade >= 18:
        cont += 1

print(f'{contm} do sexo Masculino e {contf} do sexo Feminino.')
print(f'{cont} São maiores de 18 anos.')