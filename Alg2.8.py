'''2.8. Uma distribuidora de medicamentos contratou uma software house para desenvolver um
sistema para controlar os seus processos internos. A equipe é composta por 1 analista
de  sistemas,  1  analista  de  banco  de  dados  (DBA)  e  1  desenvolvedor.  Sabendo-se  que  a
hora   de   consultoria   do   analista   de   sistemas,   do   DBA   e   do   programador   são,
respectivamente, R$ 80,00, R$ 90,00 e R$ 50,00, solicite que usuário digite a quantidade
de horas trabalhadas por cada membro da equipe e, ao fim, calcule e imprima o valor do
projeto baseado nas horas de trabalho de cada um deles.'''


a = float(input("Quantas horas você deseja contratar do Analista: "))
b = float(input("Quantas horas você deseja contratar do DBA: "))
c = float(input("Quantas horas você deseja contratar do DEV: "))

analist = 80.00 * a
dba = 90.00 * b
dev = 50.00 * c

tot = analist + dba + dev

print("Custos com cada profissional: ")
print("Analista: R$", analist)
print("DBA: R$", dba)
print("dev: R$", dev)
print("\nO total do custo será: R$", tot)