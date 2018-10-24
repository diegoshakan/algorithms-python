'''5.6. Construa um programa que armazene o gabarito da prova do Prof. Rodrigo Siqueira
que contém 10 questões e leia as opções que um aluno marcou naquela prova. Ao fim, a
aplicação deve informar o percentual de rendimento.'''

gabarito = ['A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E']
cont = 0

for c in range(10):
    resp = input(f'Digite a resposta da questão {c+1}: ').upper()
    if gabarito[c] == resp:
        cont += 1
porc = (cont * 100) / 10

print(f'O(A) aluno(a) acertou {cont} questões e teve {porc}% de acerto(s).')