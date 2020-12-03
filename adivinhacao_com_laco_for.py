print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 45
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Rodada {} de {} ".format(rodada, total_tentativas))
    chute = input("Digite o número de 0-100: ")
    numero_digitado = int(chute)
    print("Você digitou: ", chute)
    numero_valido = numero_digitado < 1 and numero_digitado >100
    if(numero_valido):
        print("Número invalido. Digite um número entre 0-100")
        continue
    acertou = numero_digitado == numero_secreto
    errou_maior = numero_digitado > numero_secreto
    errou_menor = numero_digitado < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou o número secreto!")
        break
    else:
        if (errou_maior):
            print("O número digitado é mais alto que o sorteado")

        elif (errou_menor):
            print("O numero digitado é mais baixo que o sorteado")

print("Fim de Jogo")
