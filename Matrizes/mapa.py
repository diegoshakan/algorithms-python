lin = 2
col = 2
ASSENTO = []
cont = 0

for i in range(lin):
	AUX = []
	for j in range(col):
		AUX.append(0)
	ASSENTO.append(AUX)

while  True:
	for i in range(lin):
		print(ASSENTO[i])
	if(cont == lin*col):
		print('Todos os lugares foram ocupados. ')
		break

	print('Qual assento você deseja? ')
	linha = int(input('Linha: '))
	coluna = int(input('Coluna: '))

	if (ASSENTO[linha][coluna] == 0):
		ASSENTO[linha][coluna] = 1
		cont += 1
		print('Lugar desocupado, pode sentar!')
	else:
		print('Lugar ocupado, escolha outro por favor.')