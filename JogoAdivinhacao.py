from random import randint

# Game de adivinhação. Escolha os números e o computador te dirá se você acertou o número que ele escolheu.


num = randint(1, 10)
escolha = 0
tentativas = 0
while escolha != num:
    escolha = int(input("Escolha um número entre 1 e 10 e tente advinhar o que estou pensando: "))
    tentativas += 1
    if escolha < num:
        print("O número", escolha, "é menor que o que está na minha mente.")
    elif escolha > num:
        print("O número", escolha, "é maior que o que está na minha mente.")
    else:
        print("Parabéns! você acertou com", tentativas, "tentativas.")