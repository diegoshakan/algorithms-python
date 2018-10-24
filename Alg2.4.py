'''2.4.  Construa  um  algoritmo  que  leia  2  números  reais (diferentes de  zero)
do  teclado, calcule e imprima na tela:
a) a soma dos dois valores
b) o produto deles
c) o quociente entre eles (a rotina deve criticar caso o divisor seja 0)'''

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
print('Soma:', a + b)
print('Multiplicação:', a * b)

if b == 0:
    print('Erro, não pode dividir por 0 ')
else:
    print('Divisão:', a / b)
