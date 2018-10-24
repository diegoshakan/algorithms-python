'''2.9. Construa uma aplicação que solicite ao usuário a digitação do ano
do seu nascimento. O programa deve calcular e mostrar na tela a quantidade
de dias existentes entre o ano de nascimento do usuário e o ano atual
(considere um ano com 365 dias). O formato para digitação do ano deve ser
AAAA (ex.: 1985)'''

nasc = int(input("Ano de Nascimento? "))
atual = int(input("Ano Atual? "))
idade = atual - nasc
dias = idade * 365

print("Você tem/terá", idade, "anos e viveu/viverá", dias, "dias")
