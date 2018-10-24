'''2.10. Um automóvel tem um consumo médio de 1 litro de gasolina para cada 12 km
rodados. Crie uma aplicação que solicite ao usuário a digitação da
distância percorrida em uma viagem, calcule e imprima a quantidade
de gasolina consumida durante o percurso.'''

dist = float(input('Qual a Distância em Km: '))
cons = dist / 12
print('Seu consumo de gasolina (em Litros) foi:', cons)