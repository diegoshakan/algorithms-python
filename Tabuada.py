cont = 1
cod = int(input('Qual operação você deseja: 1 - soma, 2 - subtração, 3 - multiplicaçã, 4 - divisão: '))
num = int(input('Digite um número: '))

while cont <= 10:
    if cod == 1:
        print('{} + {} = {}'.format(num, cont, (num + cont)))
        cont += 1
    if cod == 2:
        print('{} - {} = {}'.format(num, cont, (num - cont)))
        cont += 1
    if cod == 3:
        print('{} x {} = {}'.format(num, cont, (num * cont)))
        cont += 1
    if cod == 4:
        print('{} / {} = {}'.format(num, cont, (num / cont)))
        cont += 1
