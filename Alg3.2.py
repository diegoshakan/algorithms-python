'''3.2. Crie um algoritmo que leia 2 números e calcule a soma entre eles. Se o resultado for
menor que 10, somá-lo a 5; caso contrário, subtraí-lo de  7.'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

soma = a + b

if soma < 10:
    print(soma + 5)
else:
    print(soma - 7)