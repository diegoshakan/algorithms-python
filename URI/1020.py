'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, 
meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.'''

idadeDias = int(input())

ano = idadeDias // 365
resto = idadeDias % 365
meses = resto // 30
resto %= 30
dias = resto

print(ano, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')
