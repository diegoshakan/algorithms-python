'''QUESTÃO 01. Uma turma da disciplina de Banco  de  Dados possui 5 alunos. Construa  um  programa
que para cada  aluno, leia  duas  notas  e  calcule  a  média  aritmética.  Ao  fim,  de  acordo
com  a tabela  abaixo,  indique  o percentual de alunos em Prova Final.'''

rep = 0
fin = 0
apr = 0

for i in range(5):
    nota1 = float(input('Nota 1: '))
    nota2 =float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    if media < 2:
       rep += 1
    elif media >= 2 and media < 6:
        fin += 1
        perc = (fin * 100) / 5
    elif media >= 6:
        apr += 1
print(f'{fin} aluno(s) na prova final, que representam {perc}% dos alunos da turma.')
print(f'{apr} aluno(s) aprovado(s).')
print(f'{rep} aluno(s) reprovado(s)')

