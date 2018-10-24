'''4.22. Crie um algoritmo para ler o número de alunos existentes em uma turma. Em
seguida, ler o nome de cada um deles, as suas 2 notas do semestre, calcular e escrever o
nome do aluno com a maior e a menor média.'''

mediamaior = 0
mediamenor = 0
nomemenor = ''
nomemaior = ''

turma = int(input('Quantos alunos há na turma: '))

for c in range(turma):
    nome = input('Nome do Aluno: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    if c == 0:
        mediamenor = media
        mediamaior = media
        nomemaior = nome
    if media > mediamaior:
        mediamaior = media
        nomemaior = nome
    if media < mediamenor:
        mediamenor = media
        nomemenor = nome
print(f'O(A) aluno(a) {nomemaior} teve a maior média {mediamaior:.2f}')
print(f'O(A) aluno(a) {nomemenor} teve a menor média {mediamenor:.2f}')