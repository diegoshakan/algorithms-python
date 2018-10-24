'''5.1. Construa um algoritmo que leia 10 idades e calcule a média aritmética entre elas. Ao
final, mostre as idades lidas e a média encontrada.'''

idades = []
cont = 0
soma = 0

while cont < 5:
    idade = int(input('Digite uma idade: '))
    cont +=1
    soma += idade
    idades.append(idade)
#idades = idades[::-1] # somente um teste para impressão detrás para frente.
print(f'As idades são {idades}')
print(f'E a média das idades são {soma / cont:.2f}')