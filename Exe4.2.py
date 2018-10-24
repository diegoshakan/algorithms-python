'''4.2. Crie um algoritmo que leia o nome de uma pessoa e imprima este nome 50 vezes na
tela.'''

nome = input('Digite um nome: ')
cont = 0
a = 0#Coloquei este contador somente para saber quantas vezes imprimiu.
while cont <= 50:
    print(nome, a)
    cont = cont + 1
    a = a + 1