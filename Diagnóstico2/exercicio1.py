import random

def jogo_adivinhacao():
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = 8  # Número máximo que a pessoa pode tentar

    while tentativas_restantes > 0:
        try:
            
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            # Caso o jogador não digite um número
            print("Por favor, digite um número válido.")
            continue

        # Verificar se o número digitado é igual ao número secreto
        if palpite == numero_secreto:
            print("Parabéns, você acertou! :)")
            break
        elif palpite < numero_secreto:
            print("Não, o número é maior. :(")
        else:
            print("Não, o número é menor. :(")

        # Atualizar o número de tentativas
        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}")

    # Aqui é para quando esgotar as tentativas, aparecer o número secreto 
    if tentativas_restantes == 0:
        print(f"Lamento, acabaram suas oportunidades. O número era {numero_secreto}. (;-)")

# Chama a função para iniciar o jogo
jogo_adivinhacao()
