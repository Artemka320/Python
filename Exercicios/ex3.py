jogador1 = input("Jogador 1: pedra, papel ou tesoura? ")
jogador2 = input("Jogador 2: pedra, papel ou tesoura? ")

# Usa o match para decidir o vencedor
match (jogador1, jogador2):
    case ("pedra", "tesoura"):
        print("Jogador 1 ganhou!")
    case ("tesoura", "papel"):
        print("Jogador 1 ganhou!")
    case ("papel", "pedra"):
        print("Jogador 1 ganhou!")
    case ("tesoura", "pedra"):
        print("Jogador 2 ganhou!")
    case ("papel", "tesoura"):
        print("Jogador 2 ganhou!")
    case ("pedra", "papel"):
        print("Jogador 2 ganhou!")
    case _ if jogador1 == jogador2:
        print("Empate!")