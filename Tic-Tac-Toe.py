import random

board = [" " for spot in range(9)]
current_player = "X"
game_running = True
chW = False

def printboard(board):
    for row in [board[i*3 : (i+1)*3] for i in range(3)]:
        print(" | ".join(row))

def available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]

def last_player(current_player):
    return "O" if current_player == "X" else "X"

def player_move(board):
    global current_player
    square = 10
    while square not in available_moves(board):
        square = int(input(f"enter a number {current_player} (1-9): ")) - 1

    board[square] = current_player


def computer_move(board):
    global current_player
    square = random.choice(available_moves(board))
    board[square] = current_player

def AI_move(board):
    global current_player
    global last_player
    # first step
    for square in available_moves(board):
        board[square] = current_player
        if checkrows(board) or checkcolumn(board) or checkdiagnal(board):
            return
        elif not checkwin():
            board[square] = " "

    # second step
    for square in available_moves(board):
        board[square] = last_player(current_player)
        if checkrows(board) or checkcolumn(board) or checkdiagnal(board):
            board[square] = current_player
            return
        board[square] = " "

    # third step
    l1 = [i for i in [0, 2, 6, 8,] if i in available_moves(board)]
    if len(l1) > 0:
        square = random.choice(l1)
        board[square] = current_player
        return

    # fourth step
    if board[4] == " ":
        board[4] = current_player
        return

    # fifth step
    l1 = [i for i in [1, 3, 5, 7,] if i in available_moves(board)]
    if len(l1) > 0:
        square = random.choice(l1)
        board[square] = current_player

def checkrows(board):
    global game_running
    if board[0] == board[1] == board[2] and board[0] != " ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True

def checkcolumn(board):
    if board[0] == board[3] == board[6] and board[0] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return True

def checkdiagnal(board):
    if board[0] == board[4] == board[8] and board[8] != " ":
        return True
    elif  board[2] == board[4] == board[6] and board[2] != " ":
        return True

def checkwin():
    global chW
    global game_running
    if checkrows(board) or checkcolumn(board) or checkdiagnal(board):
        printboard(board)
        print(f"{current_player} won the game")
        chW = True
        game_running = False

def checktie(board):
    global game_running
    if len(available_moves(board)) == 0 and chW == False:
        printboard(board)
        print ("it is a tie")
        game_running = False

def switchplayer():
    global current_player
    current_player = "O" if current_player == "X" else "X"


start = ["C", "P"]
r = random.choice(start)

if r == "P":
    while game_running:
        printboard(board)
        player_move(board)
        checkwin()
        checktie(board)
        switchplayer()
        if game_running:
            AI_move(board)
            checkwin()
            checktie(board)
            switchplayer()

elif r == "C":
    while game_running:
        AI_move(board)
        checkwin()
        checktie(board)
        switchplayer()
        if game_running:
            printboard(board)
            player_move(board)
            checkwin()
            checktie(board)
            switchplayer()
