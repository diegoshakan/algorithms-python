'''Faça um programa que leia a velocidade e aplique uma multa caso este limite seja ultrapassado.
Fique a vontade para criar o algorítimo da multa, velocidade máxima 80km.'''

vel = int(input("Qual foi a velocidade? "))

if (vel > 80):
    print('Você ultrapassou a velocidade máxima de 80km.')
    multa = ((vel-80)*50)
    print('A sua multa vai custar R$ {:.2f}'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade!')