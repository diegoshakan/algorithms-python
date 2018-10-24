banco = {1: ['João', 333, 'P', 1000.00], 2: ['Maria', 444, 'C', 2000.00]}

def cadastrar(num, nome, cpf, conta, valor):
    banco[num] = [nome, cpf, conta, valor]
    print('Cadastro Efetuado com Sucesso')
    print('\n')

def verificar_cliente(conta, cod2):
    if cod2 == 1:
        for chave, valor in sorted(banco.items()):
            if chave == conta:
                print('Nº da Conta: ', chave, valor)
                print('\n')
    elif cod2 == 2:
        for chave, valor in sorted(banco.items()):
            print('Nº da Conta: ', chave, valor)
        print('\n')

def sacar(conta, saqvalor):
    for chave, valor in sorted(banco.items()):
        if chave == conta:
            print('Nº da Conta: ', chave, valor)
            print('\n')
            if saqvalor <= valor[3]:
                a = valor[3]
                a = a - saqvalor
                valor[3] = a
                print(f'Sr(a). {valor[0]}, Saldo da Sua Conta: ', valor[3])
                print('\n')
            else:
                print('Você não possui esse saldo.')
                print('\n')

def depositar(conta, depvalor):
    for chave, valor in sorted(banco.items()):
        if chave == conta:
           print('Nº da Conta: ', chave, valor)
           print('\n')
           if depvalor > 0:
              a = valor[3]
              a = a + depvalor
              valor[3] = a
              (print('Depósito Feito com Sucesso!'))
              print(f'Sr(a). {valor[0]}, Saldo da Sua Conta: ', valor[3])
              print('\n')
           else:
               print('Insira um valor real.')

def ver_saldo(conta):
    for chave, valor in sorted(banco.items()):
        if chave == conta:
            print(f'Seu saldo Sr(a). {valor[0]} é: R$ {valor[3]} ')
            print('\n')

def remover(conta):
    for chave, valor in sorted(banco.items()):
        if chave == conta:
            banco.pop(conta)
            print(f'--- Conta {conta} do Sr(a). {valor[0]} removida com sucesso. ---\n')

def transferir(conta1, conta2, transvalor):
    for chave, valor in sorted(banco.items()):
        if chave == conta1:
            if transvalor <= valor[3]:
                a = valor[3]
                a = a - transvalor
                valor[3] = a
        if chave == conta2:
            if transvalor > 0:
                a = valor[3]
                a = a + transvalor
                valor[3] = a
            print(f'Você Transferiu R$ {transvalor} para Conta: {conta2} do(a) Sr(a). {valor[0]}')
            print('\n')
#Programa Principal

while True:
    print('1. Cadastrar Cliente\n2. Verificar Cliente \n3. Saque\n4. Depósito\n5. Saldo\n6. Transferir\n7. Remover Cliente\n0. Sair do Programa:')
    cod = int(input('\nDigite a opção: '))
    print('')

    if cod == 0:
        print('Volte Sempre!')
        break

    elif cod == 1:
        num = int(input('Número da conta: '))
        nome = input('Nome: ').title()
        cpf = input('CPF: ')
        conta = input('Tipo de Conta (P/C): ').capitalize()
        valor = float(input('Valor inicial: '))
        cadastrar(num, nome, cpf, conta, valor)

    elif cod == 2:
        print('1. Consultar Cliente\n2. Consultar Todas as Contas')
        cod2 = int(input('Digite a Opção: '))
        print('\n')
        if cod2 == 1:
            conta = int(input('Insira a conta a ser consultada: '))
            verificar_cliente(conta, cod2)
        elif cod2 == 2:
            conta = 0
            verificar_cliente(conta, cod2)

    elif cod == 3:
        conta = int(input('Conta que Deseja Sacar: '))
        saqvalor = float(input('Qual valor: '))
        sacar(conta, saqvalor)

    elif cod == 4:
        conta = int(input('Conta que Deseja Depositar: '))
        depvalor = float(input('Qual valor: '))
        depositar(conta, depvalor)

    elif cod == 5:
        conta = int(input('Conta que Deseja Ver Saldo: '))
        ver_saldo(conta)

    elif cod == 6:
        conta1 = int(input('De Qual Conta Você Deseja Transferir: '))
        conta2 = int(input('Para Qual Conta Você Deseja Transferir: '))
        transvalor = float(input('Qunato Deseja Transferir: '))
        transferir(conta1, conta2, transvalor)

    elif cod == 7:
        conta = int(input('Qual Conta Você Deseja Remover: '))
        remover(conta)