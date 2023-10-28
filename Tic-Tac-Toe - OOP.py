import random
import time


class TicTacToe():
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.winner = None

    def empty_squares(self):
        return self.board.count(' ')

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print(" | ".join(row))

    def move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.checkwinner(letter):
                self.winner = letter

    def checkwinner(self, letter):
        winning_position = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
            0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        for position in winning_position:
            if all(self.board[i] == letter for i in position):
                return True
        return False

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


class Player():
    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            square = int(input("enter a number (1-9): ")) - 1
            if square in game.available_moves():
                return square


class ComPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # step 1
        for square in game.available_moves():
            game.board[square] = "X"
            if game.checkwinner(letter="X"):
                game.board[square] = " "
                time.sleep(1)
                return square
            elif not game.checkwinner(letter="X"):
                game.board[square] = " "

        # step 2
        for square in game.available_moves():
            game.board[square] = "O"
            if game.checkwinner(letter="O"):
                game.board[square] = " "
                time.sleep(1)
                return square
            elif not game.checkwinner(letter="O"):
                game.board[square] = " "

        # step 3
        l1 = [i for i in [0, 2, 6, 8,] if i in game.available_moves()]
        if len(l1) > 0:
            square = random.choice(l1)
            time.sleep(1)
            return square

        # step 4
        if game.board[4] == " ":
            time.sleep(1)
            return square

        # step 5
        l1 = [i for i in [1, 3, 5, 7,] if i in game.available_moves()]
        if len(l1) > 0:
            square = random.choice(l1)
            time.sleep(1)
            return square


def play(game, x_player, o_player, game_running=True):
    if game_running:
        game.print_board()

    l = ["O", "X"]
    letter = random.choice(l)
    while game_running:
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        game.move(square, letter)

        if game_running:
            game.print_board()
        if game.winner:
            print(letter + " wins!")
            return letter

        letter = "O" if letter == "X" else "X"
        if game.empty_squares() == 0:
            print("It is a Tie!")
            return


t = TicTacToe()
x_player = ComPlayer("X")
o_player = HumanPlayer("O")
play(t, x_player, o_player, game_running=True)
