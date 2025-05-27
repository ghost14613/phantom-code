import chess

def jogar_xadrez():
    print("Digite movimentos no formato UCI (ex: e2e4, b1c3)")
    print("Digite 'sair' para encerrar.\n")

    board = chess.Board()  

    while not board.is_game_over():
        print(board)
        print("Turno das peças", "brancas" if board.turn else "pretas")

        movimento = input("Seu movimento: ").strip().lower()

        if movimento == "sair":
            break

        try:
            lance = chess.Move.from_uci(movimento)
            if lance in board.legal_moves:
                board.push(lance)
            else:
                print("Movimento ilegal. Tente novamente.\n")
        except:
            print("Formato inválido. Use algo como e2e4.\n")

    print("\nFim de jogo!")
    print("Motivo:", board.result(), "-", board.outcome().termination.name)

if __name__ == "__main__":
    jogar_xadrez()
