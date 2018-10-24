'''3.3. Crie um algoritmo que receba 2 números e a operação que será executada sobre eles
(soma, subtração, multiplicação ou divisão). Calcule o resultado da operação e mostre na
tela.'''

cod = int(input('Digite um número, 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: '))

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if cod == 1:
    print('Soma', a + b)
elif cod == 2:
    print('Subtração', a - b)
elif cod == 3:
    print('Multiplicação', a * b)
elif cod == 4:
    print('Divisão', a / b)  # se o segundo número for '0' o Pycharm apresenta automaticamente o erro.
else:
    print('Código Inválido!')
