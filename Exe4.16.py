from time import sleep
'''4.16. Imagine que o par usuário/senha de um login de administrador de redes de uma
empresa seja, respectivamente, chiclete/nana. Crie uma rotina para validar o acesso de
um usuário à rede, porém com a seguinte restrição:
se ele errar a senha mais de 3 vezes, mostrar a mensagem:
“Usuário bloqueado! Favor, contactar administrador de rede.”
se o par usuário/senha forem validados, mostrar a mensagem:
“Seja bem-vindo.”'''

block = 0

while block != 3:
    usuario = input('Nome de Usuário: ')
    senha = input('Senha: ')
    if usuario == 'chiclete' and senha == 'nana':
        print('\"Seja bem-vindo.\"')
        break
    elif usuario != 'chiclete' and senha != 'nana':
        print('Senha inválida, por favor digite corretamente.')
    block += 1
    if block == 3:
        sleep(0.5)
        print('\"Usuário bloqueado! Favor, contactar administrador de rede.\"')