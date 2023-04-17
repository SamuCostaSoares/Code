def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end = " ")
        for j in range(3):
            print(board[i][j], "|", end = " ")
        print()
        print("-------------")
# parâmetro e imprime uma representação visual do jogo da velha 

def check_win(board, mark):
    for i in range(3):
        if (board[i][0] == mark and board[i][1] == mark and board[i][2] == mark):
            return True
        if (board[0][i] == mark and board[1][i] == mark and board[2][i] == mark):
            return True
    if (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark):
        return True
    if (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    return False
# lógica de verificação de vitória check_win, que recebe dois argumentos: board (tabuleiro) e mark (marca). 

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    winner = False
    while not winner:
        print_board(board)
        row = int(input("Digite o número da linha (0, 1 ou 2): "))
        col = int(input("Digite o número da coluna (0, 1 ou 2): "))
        if (board[row][col] == " "):
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print("Parabéns, o jogador " + player + " ganhou!")
                winner = True
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"
        else:
            print("Esta posição já foi escolhida. Por favor, escolha outra.")
            
tic_tac_toe()
# jogador atual é alternado para o outro jogador e o loop continua