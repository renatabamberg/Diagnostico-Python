import random

def jogoAdivinhacao():

    print("Bem vindo ao jogo de adivinhação")
    print("Pense em um valor inteiro aleatório de 1 à 100 para eu adivinhar")

    tentativas_restantes = 8  # Número máximo que a maquina pode tentar

    while tentativas_restantes > 0:
        
        palpite = random.randint(1, 100)
        print(f"Seu número é {palpite}? Se for igual digite 0; se for menor digite 1, se for maior digite 2")
        resposta = int(input("Digite sua resposta: "))
  
        if resposta == 0:
            print("Parabéns, você acertou! :)")
            break
        elif palpite == 2:
            print("Não, o número é maior. :(")
        else:
            print("Não, o número é menor. :(")

        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}")

    if tentativas_restantes == 0:
        print(f"Lamento, acabaram suas oportunidades.")

# Chama a função para iniciar o jogo
jogoAdivinhacao()

