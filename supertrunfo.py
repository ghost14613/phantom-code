import random

class Carta:
    def __init__(self, nome, forca, velocidade, inteligencia):
        self.nome = nome
        self.atributos = {
            "Força": forca,
            "Velocidade": velocidade,
            "Inteligência": inteligencia
        }

    def __str__(self):
        return f"{self.nome} - Força: {self.atributos['Força']}, Velocidade: {self.atributos['Velocidade']}, Inteligência: {self.atributos['Inteligência']}"

class JogoSuperTrunfo:
    def __init__(self):
        self.baralho = [
            Carta("Dragão", 90, 70, 80),
            Carta("Tigre", 80, 90, 60),
            Carta("Robô", 70, 50, 95),
            Carta("Mago", 60, 40, 99),
            Carta("Guerreiro", 85, 80, 75)
        ]
        random.shuffle(self.baralho)
        meio = len(self.baralho) // 2
        self.jogador1 = self.baralho[:meio]
        self.jogador2 = self.baralho[meio:]

    def jogar_rodada(self):
        if not self.jogador1 or not self.jogador2:
            return None  # O jogo acabou
        
        carta1 = self.jogador1.pop(0)
        carta2 = self.jogador2.pop(0)
        
        print("\nJogador 1 tem a carta:")
        print(carta1)
        print("\nJogador 2 tem a carta:")
        print(carta2)
        
        atributo = random.choice(list(carta1.atributos.keys()))
        print(f"Atributo escolhido: {atributo}")
        
        if carta1.atributos[atributo] > carta2.atributos[atributo]:
            print("Jogador 1 vence a rodada!")
            self.jogador1.append(carta1)
            self.jogador1.append(carta2)
        elif carta1.atributos[atributo] < carta2.atributos[atributo]:
            print("Jogador 2 vence a rodada!")
            self.jogador2.append(carta1)
            self.jogador2.append(carta2)
        else:
            print("Empate! Cada jogador mantém sua carta.")
            self.jogador1.append(carta1)
            self.jogador2.append(carta2)
    
    def jogar(self):
        rodada = 1
        while self.jogador1 and self.jogador2:
            print(f"\n===== Rodada {rodada} =====")
            self.jogar_rodada()
            rodada += 1
            input("Pressione Enter para continuar...")
        
        if self.jogador1:
            print("\nJogador 1 venceu o jogo!")
        else:
            print("\nJogador 2 venceu o jogo!")

if __name__ == "__main__":
    jogo = JogoSuperTrunfo()
    jogo.jogar()

