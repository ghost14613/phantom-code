import random

TAMANHO = 5
NUM_NAVIOS = 3

def criar_tabuleiro():
    return [["~"] * TAMANHO for _ in range(TAMANHO)]

def imprimir_tabuleiro(tabuleiro, ocultar=False):
    print("  " + " ".join([str(i) for i in range(TAMANHO)]))
    for idx, linha in enumerate(tabuleiro):
        linha_visivel = [("~" if (cel == "N" and ocultar) else cel) for cel in linha]
        print(f"{idx} " + " ".join(linha_visivel))

def posicionar_navios(tabuleiro):
    navios = 0
    while navios < NUM_NAVIOS:
        linha = random.randint(0, TAMANHO - 1)
        coluna = random.randint(0, TAMANHO - 1)
        if tabuleiro[linha][coluna] != "N":
            tabuleiro[linha][coluna] = "N"
            navios += 1

def atirar(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == "N":
        tabuleiro[linha][coluna] = "X"
        return "Acertou!"
    elif tabuleiro[linha][coluna] == "~":
        tabuleiro[linha][coluna] = "O"
        return "Água."
    else:
        return "Você já atirou aqui."

def contar_acertos(tabuleiro):
    return sum(linha.count("X") for linha in tabuleiro)

def turno_jogador(tabuleiro_inimigo):
    while True:
        try:
            linha = int(input("Escolha a linha (0 a 4): "))
            coluna = int(input("Escolha a coluna (0 a 4): "))
            if 0 <= linha < TAMANHO and 0 <= coluna < TAMANHO:
                resultado = atirar(tabuleiro_inimigo, linha, coluna)
                print(resultado)
                break
            else:
                print("Coordenadas inválidas. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Use números inteiros.")

def turno_computador(tabuleiro):
    while True:
        linha = random.randint(0, TAMANHO - 1)
        coluna = random.randint(0, TAMANHO - 1)
        if tabuleiro[linha][coluna] not in ["X", "O"]:
            print(f"Computador atirou em ({linha}, {coluna})")
            resultado = atirar(tabuleiro, linha, coluna)
            print(resultado)
            break

def main():
    print("🌊 BATALHA NAVAL - Python 🌊")

    jogador = criar_tabuleiro()
    computador = criar_tabuleiro()
    posicionar_navios(jogador)
    posicionar_navios(computador)

    while True:
        print("\nSeu Tabuleiro:")
        imprimir_tabuleiro(jogador)
        print("\nTabuleiro do Computador:")
        imprimir_tabuleiro(computador, ocultar=True)

        print("\n🔫 Sua vez!")
        turno_jogador(computador)

        if contar_acertos(computador) == NUM_NAVIOS:
            print("🎉 Você venceu!")
            break

        print("\n💻 Vez do computador...")
        turno_computador(jogador)

        if contar_acertos(jogador) == NUM_NAVIOS:
            print("💥 O computador venceu!")
            break

if __name__ == "__main__":
    main()
