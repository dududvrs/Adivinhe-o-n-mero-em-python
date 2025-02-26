import random
import time
def jogo_adivinhacao():

    random.seed(time.time())

    numero_secreto = random.randint(1, 100)

    tentativas = 0
    acertou = False

    print("Seja Bem vindo ao Jogo!")
    print("Tente a sorte e tente adivinhar o número secreto entre 1 e 100.")



    while not acertou:
        tentativas += 1
        palpite = int(input("Digite seu palpite: "))

        

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            acertou = True
        else:
            diferenca = abs(palpite - numero_secreto)

            if diferenca <= 2:
                print("Pelando!")
            elif diferenca <= 4:
                print("Tá muito perto!")
            elif diferenca <= 8:
                print("Tá perto até!")
            elif diferenca <= 10:
                print("Xii! esfriô!")
            else:
                    if palpite > numero_secreto:
                            print("Seu paltite tá muito alto!")
                    else:
                            print("Seu palpite foi muito baixo!")
# Iniciar o jogo
jogo_adivinhacao()