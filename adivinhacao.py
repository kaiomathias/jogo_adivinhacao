print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 45
total_tentativas = 3
rodada = 1
while (total_tentativas > 0):
    print("Rodada {} de {} ".format(rodada, total_tentativas))
    chute = input("Digite o seu número: ")
    numero_digitado = int(chute)
    print("Você digitou: ", chute)
    acertou = numero_digitado == numero_secreto
    errou_maior = numero_digitado > numero_secreto
    errou_menor = numero_digitado < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou o número secreto!")
        total_tentativas =0
    else:
        if (errou_maior):
            print("O número digitado é mais alto que o sorteado")
            total_tentativas -= 1

        elif (errou_menor):
            print("O numero digitado é mais baixo que o sorteado")
    rodada += 1

print("Fim de Jogo")
