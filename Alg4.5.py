'''Escreva um programa que escreva a distância que um passageiro deseja percorrer em KM.
Calcule o preço da passagem cobrando R$ 0,50 por KM para viajantes de até 200km, e R$ 0,45
para viagens mais longas.'''

dist = int(input('Qual a distância da viagem: '))

if dist <= 200:
    valor = (dist * 0.5)
else:
    valor = (dist * 0.45)

print('Sua passagem custará R$ {}'.format(valor))



