'''Crie um programa que leia três números e diga qual é o maior e o menor deles.'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

if a > b and a > c:
    print('O primeiro número é o maior {}'.format(a))
elif b > a and b > c:
    print('O segundo número é o maior {}'.format(b))
else:
    print('O terceiro número é o maior {}'.format(c))

if a < b and a < c:
    print('O primeiro número é o menor {}'.format(a))
elif b < a and b < c:
    print('O segundo número é o menor {}'.format(b))
else:
    print('O terceiro número é o menor {}'.format(c))



'''Outra forma de fazer a questão acima.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

maior = a
menor = a

if maior < b:
    maior = b
if maior < c:
    maior = c
if menor > b:
    menor = b
if menor > c:
    menor = c

print(maior)
print(menor)'''