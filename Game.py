import os


class Game:

    board = []
    turn = 1
    width = None
    hints = True
    header = None
    possible_moves = None
    piece_row = None
    piece_column = None
    
    def __init__(self):
        #fill the array to create the initial state of the board
        for i in range(8):
            self.board.append(["-"] * 8)
        
        self.board[3][3] = "X"
        self.board[3][4] = "O"
        self.board[4][3] = "O"
        self.board[4][4] = "X"

        #get the width of the terminal
        self.width = os.get_terminal_size().columns - 1 

    def ask_hints(self):
        while True:
            print()
            user_input = input("Would you like to enable hints Y/N: ")
            if user_input == "Y" or user_input == "y":
                self.hints = True
                break
            elif user_input == "N" or user_input == "n":
                self.hints = False
                break
            else:
                print()
                print("Please enter Y or N.")
                continue

    def print_board(self):
        header = ""
        for i in range(1,9):
            header += " " + str(i)
        print(header.center(self.width))

        for i in range(1,9):
            print((str(i) + " " + " ".join(self.board[i - 1])).center(self.width))

    def clear_past_available_moves(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == "#":
                    self.board[i][j] = "-"

    def available_moves(self, opp_player, player):
        for i in range(8):
            for j in range(7):
                if self.board[i][j] == opp_player and self.board[i][j + 1] == "-":
                    for k in range(8):
                        count1 = 0
                        if self.board[i][k] == player:
                            if j > k:
                                if j - k == 1:
                                    self.board[i][j + 1] = "#"
                                else:
                                    for t in range(1,j - k):
                                        if self.board[i][k + t] == opp_player:
                                            count1 += 1
                                        if count1 == j - k - 1:
                                            self.board[i][j + 1] = "#"
        for i in range(8):
            for j in range(1,8):
                if self.board[i][j] == opp_player and self.board[i][j - 1] == "-":
                    for k in range(8):
                        count2 = 0
                        if self.board[i][k] == player:
                            if k > j:
                                if k - j == 1:
                                    self.board[i][j - 1] = "#"
                                else:
                                    for t in range(1,k - j):
                                        if self.board[i][k - t] == opp_player:
                                            count2 += 1
                                        if count2 == k - j - 1:
                                            self.board[i][j - 1] = "#"
        for i in range(7):
            for j in range(8):
                if self.board[i][j] == opp_player and self.board[i + 1][j] == "-":
                    for k in range(8):
                        count3 = 0
                        if self.board[k][j] == player:
                            if i > k:
                                if i - k == 1:
                                    self.board[i + 1][j] = "#"
                                else:
                                    for t in range(1,i - k):
                                        if self.board[k + t][j] == opp_player:
                                            count3 += 1
                                        if count3 == i - k - 1:
                                            self.board[i + 1][j] = "#"
        for i in range(1,8):
            for j in range(8):
                if self.board[i][j] == opp_player and self.board[i - 1][j] == "-":
                    for k in range(8):
                        count4 = 0
                        if self.board[k][j] == player:
                            if k > i:
                                if k - i == 1:
                                    self.board[i - 1][j] = "#"
                                else:
                                    for t in range(1,k - i):
                                        if self.board[k - t][j] == opp_player:
                                            count4 += 1
                                        if count4 == k - i - 1:
                                            self.board[i - 1][j] = "#"
        for i in range(1,7):
            for j in range(1,7):
                if self.board[i][j] == opp_player and self.board[i + 1][j + 1] == "-":
                    if i < j:
                        for k in range(1,i + 1):
                            count5 = 0
                            if self.board[i - k][j - k] == player:
                                if k == 1:
                                    self.board[i + 1][j + 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i - t][j - t] == opp_player:
                                            count5 += 1
                                        if count5 == k - 1:
                                            self.board[i + 1][j + 1] = "#"
                    if i >= j:
                        for k in range(1,j + 1):
                            count6 = 0
                            if self.board[i - k][j - k] == player:
                                if k == 1:
                                    self.board[i + 1][j + 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i - t][j - t] == opp_player:
                                            count6 += 1
                                        if count6 == k - 1:
                                            self.board[i + 1][j + 1] = "#"
        for i in range(1,7):
            for j in range(1,7):
                if self.board[i][j] == opp_player and self.board[i - 1][j - 1] == "-":
                    if i < j:
                        for k in range(1,8 - j):
                            count7 = 0
                            if self.board[i + k][j + k] == player:
                                if k == 1:
                                    self.board[i - 1][j - 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i + t][j + t] == opp_player:
                                            count7 += 1
                                        if count7 == k - 1:
                                            self.board[i - 1][j - 1] = "#"
                    if i >= j:
                        for k in range(1,8 - i):
                            count8 = 0
                            if self.board[i + k][j + k] == player:
                                if k == 1:
                                    self.board[i - 1][j - 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i + t][j + t] == opp_player:
                                            count8 += 1
                                        if count8 == k - 1:
                                            self.board[i - 1][j - 1] = "#"
        for i in range(1,7):
            for j in range(1,7):
                if self.board[i][j] == opp_player and self.board[i - 1][j + 1] == "-":
                    if 7 - i < j:
                        for k in range(1,8 - i):
                            count9 = 0
                            if self.board[i + k][j - k] == player:
                                if k == 1:
                                    self.board[i - 1][j + 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i + t][j - t] == opp_player:
                                            count9 += 1
                                        if count9 == k - 1:
                                            self.board[i - 1][j + 1] = "#"
                    if 7 - i >= j:
                        for k in range(1,j + 1):
                            count10 = 0
                            if self.board[i + k][j - k] == player:
                                if k == 1:
                                    self.board[i - 1][j + 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i + t][j - t] == opp_player:
                                            count10 += 1
                                        if count10 == k - 1:
                                            self.board[i - 1][j + 1] = "#"
        for i in range(1,7):
            for j in range(1,7):
                if self.board[i][j] == opp_player and self.board[i + 1][j - 1] == "-":
                    if 7 - i < j:
                        for k in range(1,8 - j):
                            count11 = 0
                            if self.board[i - k][j + k] == player:
                                if k == 1:
                                    self.board[i + 1][j - 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i - t][j + t] == opp_player:
                                            count11 += 1
                                        if count11 == k - 1:
                                            self.board[i + 1][j - 1] = "#"
                    if 7 - i >= j:
                        for k in range(1,i + 1):
                            count12 = 0
                            if self.board[i - k][j + k] == player:
                                if k == 1:
                                    self.board[i + 1][j - 1] = "#"
                                else:
                                    for t in range(1,k):
                                        if self.board[i - t][j + t] == opp_player:
                                            count12 += 1
                                        if count12 == k - 1:
                                            self.board[i + 1][j - 1] = "#"
        self.possible_moves = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == "#":
                    self.possible_moves += 1
        return self.possible_moves

    def any_possible_moves(self):
        self.clear_past_available_moves()
        store1 = self.available_moves("X", "O")
        self.clear_past_available_moves()
        store2 = self.available_moves("O", "X")
        if store1 + store2 == 0:
            return 0

    def place_piece(self, player):
        check = 0
        while check == 0:
            count = 0
            while count == 0:
                print()
                self.piece_row = input("Player " + player + ", choose a row in which to place your piece: ")
                if self.piece_row.isnumeric() == True:
                    self.piece_row = int(self.piece_row)
                    if self.piece_row <= 8 and self.piece_row >= 1:
                        self.piece_row = self.piece_row - 1
                        count += 1
                    else:
                        print()
                        print("Please enter an integer between 1 and 8.")
                else:
                    print()
                    print("Please enter an integer between 1 and 8.")
            count = 0
            while count == 0:
                print()
                self.piece_column = input("Player " + player + ", choose a column in which to place your piece: ")
                if self.piece_column.isnumeric() == True:
                    self.piece_column = int(self.piece_column)
                    if self.piece_column <= 8 and self.piece_column >= 1:
                        self.piece_column = self.piece_column - 1
                        count += 1
                    else:
                        print()
                        print("Please enter an integer between 1 and 8.")
                else:
                    print()
                    print("Please enter an integer between 1 and 8.")
            if self.board[self.piece_row][self.piece_column] == "#":
                self.board[self.piece_row][self.piece_column] = player
                check += 1
            else:
                print()
                print("That is not a valid move. Please go again.")

    def change_pieces(self, opp_player, player):
        count = [0] * 12

        for i in range(1,7 - self.piece_column):
            if self.board[self.piece_row][self.piece_column + i] == opp_player and self.board[self.piece_row][self.piece_column + i + 1] == player:
                if i == 1:
                    self.board[self.piece_row][self.piece_column + i] = player
                else:
                    for j in range(1,i):
                        if self.board[self.piece_row][self.piece_column + i - j] == opp_player:
                            count[0] += 1
                        if count[0] == i - 1:
                            for k in range(1,i + 1):
                                self.board[self.piece_row][self.piece_column + k] = player
                break
        for i in range(1,7 - self.piece_row):
            if self.board[self.piece_row + i][self.piece_column] == opp_player and self.board[self.piece_row + i + 1][self.piece_column] == player:
                if i == 1:
                    self.board[self.piece_row + i][self.piece_column] = player
                else:
                    for j in range(1,i):
                        if self.board[self.piece_row + i - j][self.piece_column] == opp_player:
                            count[1] += 1
                        if count[1] == i - 1:
                            for k in range(1,i + 1):
                                self.board[self.piece_row + k][self.piece_column] = player
                break
        for i in range(1, self.piece_column):
            if self.board[self.piece_row][self.piece_column - i] == opp_player and self.board[self.piece_row][self.piece_column - i - 1] == player:
                if i == 1:
                    self.board[self.piece_row][self.piece_column - i] = player
                else:
                    for j in range(1,i):
                        if self.board[self.piece_row][self.piece_column - i + j] == opp_player:
                            count[2] += 1
                        if count[2] == i - 1:
                            for k in range(1,i + 1):
                                self.board[self.piece_row][self.piece_column - k] = player
                break
        for i in range(1, self.piece_row):
            if self.board[self.piece_row - i][self.piece_column] == opp_player and self.board[self.piece_row - i - 1][self.piece_column] == player:
                if i == 1:
                    self.board[self.piece_row - i][self.piece_column] = player
                else:
                    for j in range(1,i):
                        if self.board[self.piece_row - i + j][self.piece_column] == opp_player:
                            count[3] += 1
                        if count[3] == i - 1:
                            for k in range(1,i + 1):
                                self.board[self.piece_row - k][self.piece_column] = player
                break
        if self.piece_row + self.piece_column >= 7:
            for i in range(1,7 - self.piece_column):
                if self.board[self.piece_row - i][self.piece_column + i] == opp_player and self.board[self.piece_row - i - 1][self.piece_column + i + 1] == player:
                    if i == 1:
                        self.board[self.piece_row - i][self.piece_column + i] = player
                    else:
                        for j in range(1,i):
                            if self.board[self.piece_row - i + j][self.piece_column + i - j] == opp_player:
                                count[4] += 1
                            if count[4] == i - 1:
                                for k in range(1,i + 1):
                                    self.board[self.piece_row - k][self.piece_column + k] = player
                    break
            for i in range(1,7 - self.piece_row):
                if self.board[self.piece_row + i][self.piece_column - i] == opp_player and self.board[self.piece_row + i + 1][self.piece_column - i - 1] == player:
                    if i == 1:
                        self.board[self.piece_row + i][self.piece_column - i] = player
                    else:
                        for j in range(1,i):
                            if self.board[self.piece_row + i - j][self.piece_column - i + j] == opp_player:
                                count[5] += 1
                            if count[5] == i - 1:
                                for k in range(1,i + 1):
                                    self.board[self.piece_row + k][self.piece_column - k] = player
                    break
        else:
            for i in range(1,self.piece_row):
                if self.board[self.piece_row - i][self.piece_column + i] == opp_player and self.board[self.piece_row - i - 1][self.piece_column + i + 1] == player:
                    if i == 1:
                        self.board[self.piece_row - i][self.piece_column + i] = player
                    else:
                        for j in range(1,i):
                            if self.board[self.piece_row - i + j][self.piece_column + i - j] == opp_player:
                                count[6] += 1
                            if count[6] == i - 1:
                                for k in range(1,i + 1):
                                    self.board[self.piece_row - k][self.piece_column + k] = player
            for i in range(1, self.piece_column):
                if self.board[self.piece_row + i][self.piece_column - i] == opp_player and self.board[self.piece_row + i + 1][self.piece_column - i - 1] == player:
                    if i == 1:
                        self.board[self.piece_row + i][self.piece_column - i] = player
                    else:
                        for j in range(1, i):
                            if self.board[self.piece_row + i - j][self.piece_column - i + j] == opp_player:
                                count[7] += 1
                            if count[7] == i - 1:
                                for k in range(1,i + 1):
                                    self.board[self.piece_row + k][self.piece_column - k] = player
                    break
        if self.piece_row > self.piece_column:
            for i in range(1,7 - self.piece_row):
                if self.board[self.piece_row + i][self.piece_column + i] == opp_player and self.board[self.piece_row + i + 1][self.piece_column + i + 1] == player:
                    if i == 1:
                        self.board[self.piece_row + i][self.piece_column + i] = player
                    else:
                        for j in range(1,i):
                            if self.board[self.piece_row + i - j][self.piece_column + i - j] == opp_player:
                                count[8] += 1
                            if count[8] == i - 1:
                                for k in range(1,i + 1):
                                    self.board[self.piece_row + k][self.piece_column + k] = player
                    break
            for i in range(1, self.piece_column):
                if self.board[self.piece_row - i][self.piece_column - i] == opp_player and self.board[self.piece_row - i - 1][self.piece_column - i - 1] == player:
                    if i == 1:
                        self.board[self.piece_row - i][self.piece_column - i] = player
                    else:
                        for j in range(1, i):
                            if self.board[self.piece_row - i + j][self.piece_column - i + j] == opp_player:
                                count[9] += 1
                            if count[9] == i - 1:
                                for k in range(1, i + 1):
                                    self.board[self.piece_row - k][self.piece_column - k] = player
                    break
        else:
            for i in range(1,7 - self.piece_column):
                if self.board[self.piece_row + i][self.piece_column + i] == opp_player and self.board[self.piece_row + i + 1][self.piece_column + i + 1] == player:
                    if i == 1:
                        self.board[self.piece_row + i][self.piece_column + i] = player
                    else:
                        for j in range(1, i):
                            if self.board[self.piece_row + i - j][self.piece_column + i - j] == opp_player:
                                count[10] += 1
                            if count[10] == i - 1:
                                for k in range(1, i + 1):
                                    self.board[self.piece_row + k][self.piece_column + k] = player
            for i in range(1, self.piece_row):
                if self.board[self.piece_row - i][self.piece_column - i] == opp_player and self.board[self.piece_row - i - 1][self.piece_column - i - 1] == player:
                    if i == 1:
                        self.board[self.piece_row - i][self.piece_column - i] = player
                    else:
                        for j in range(1,i):
                            if self.board[self.piece_row - i + j][self.piece_column - i + j] == opp_player:
                                count[11] += 1
                            if count[11] == i - 1:
                                for k in range(1, i + 1):
                                    self.board[self.piece_row - k][self.piece_column - k] = player
                    break

    def check_board(self):
        Xcount = 0
        Ocount = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == "X":
                    Xcount += 1
                elif self.board[i][j] == "O":
                    Ocount += 1
        if any_possible_moves() == 0:
            Xcount = str(Xcount)
            Ocount = str(Ocount)
            print()
            print("X has " + Xcount + " spaces.")
            print()
            print("O has " + Ocount + " spaces.")
            if Xcount > Ocount:
                print()
                print("Player X is the winner!")
            elif Xcount < Ocount:
                print()
                print("Player O is the winner!")
            else:
                print()
                print("It's a tie!")
            
            while yn_tracker == 0:
                print()
                yn = input("Would you like to play again? Please enter Y or N. ")
                if len(yn) != 1:
                    print()
                    print("Please enter Y or N.")
                elif yn == "Y" or yn =="y":
                    for x in range(8):
                        for y in range(8):
                            self.board[x][y] = "-"
                    self.board[3][3] = "X"
                    self.board[3][4] = "O"
                    self.board[4][3] = "O"
                    self.board[4][4] = "X"
                    self.turn = 1
                    yn_tracker = 1
                elif yn =="N" or yn =="n":
                    self.turn  = 0
                    print()
                    print("Goodbye!")
                    yn_tracker = 1
                else:
                    print()
                    print("Please enter Y or N.")
