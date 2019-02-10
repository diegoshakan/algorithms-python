# ler um valor

n = int(input())

# verificar valores

nota100 = n // 100
r = n % 100

nota50 = r // 50
r %= 50

nota20 = r // 20
r %= 20

nota10 = r // 10
r %= 10

nota5 = r // 5
r %= 5

nota2 = r // 2

nota1 = r%2

print(n)
print(nota100, 'nota(s) de R$ 100,00')
print(nota50, 'nota(s) de R$ 50,00')
print(nota20, 'nota(s) de R$ 20,00')
print(nota10, 'nota(s) de R$ 10,00')
print(nota5, 'nota(s) de R$ 5,00')
print(nota2, 'nota(s) de R$ 2,00')
print(nota1, 'nota(s) de R$ 1,00')