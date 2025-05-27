import random

# Definindo algumas cartas com atributos
cartas = [
    {"nome": "Dragão", "força": 90, "velocidade": 70, "inteligência": 60},
    {"nome": "Fênix", "força": 75, "velocidade": 95, "inteligência": 85},
    {"nome": "Golem", "força": 100, "velocidade": 40, "inteligência": 50},
    {"nome": "Grifo", "força": 80, "velocidade": 80, "inteligência": 70},
    {"nome": "Unicórnio", "força": 60, "velocidade": 85, "inteligência": 90},
]

# Distribui uma carta para cada jogador
carta_jogador = random.choice(cartas)
carta_cpu = random.choice(cartas)

# Mostra a carta do jogador
print("Sua carta:")
for atributo, valor in carta_jogador.items():
    print(f"{atributo.capitalize()}: {valor}")

# Jogador escolhe o atributo
atributo_escolhido = input("\nEscolha um atributo (força, velocidade, inteligência): ").lower()

# Verifica se o atributo é válido
if atributo_escolhido not in ["força", "velocidade", "inteligência"]:
    print("Atributo inválido. Fim de jogo.")
else:
    valor_jogador = carta_jogador[atributo_escolhido]
    valor_cpu = carta_cpu[atributo_escolhido]

    print("\nCarta do oponente:")
    for atributo, valor in carta_cpu.items():
        print(f"{atributo.capitalize()}: {valor}")

    print(f"\nVocê escolheu o atributo: {atributo_escolhido.capitalize()}")
    print(f"Seu valor: {valor_jogador}")
    print(f"Valor do CPU: {valor_cpu}")

    # Verifica o vencedor
    if valor_jogador > valor_cpu:
        print(" Você venceu a rodada!")
    elif valor_jogador < valor_cpu:
        print(" Você perdeu a rodada.")
    else:
        print(" Empate!")
