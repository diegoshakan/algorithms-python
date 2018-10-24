cont = 1
fat = 1
num = int(input('Digite um número: '))
while cont <= num:
    fat = fat * cont
    cont = cont + 1
    print(fat, end = ' ' )