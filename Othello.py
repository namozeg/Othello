#!/bin/python3

board = []
turn = 1

for i in range(8):
    board.append(["-"] * 8)

board[3][3] = "X"
board[3][4] = "O"
board[4][3] = "O"
board[4][4] = "X"

import os  
width = os.get_terminal_size().columns - 1

print()
print("Othello".center(width))
print("by namozeg".center(width))
print()
print("Welcome to Othello, a two-player tile-flipping game! Take turns placing pieces".center(width))
print("on the board that flank oppponent pieces to capture them and turn them into your".center(width))
print("own. Pieces can be flanked horizontally, vertically, and even diagonally. Note".center(width))
print("that you can only place a piece if it captures at least one opponent piece. If you".center(width))
print("have no available moves, your turn will be skipped. If neither player has an available".center(width))
print("move, the game is over. Whoever has more tiles at the end of the game is the winner.".center(width))

print("Good luck!".center(width))
print()
print("For questions, comments, or edits, please email me at namozeg@gmail.com".center(width))

def ask_hints():
    global hints
    while True:
        print()
        hints = input("Would you like to enable hints for this game? Please enter Y or N. ")
        if hints == "Y" or hints == "y":
            hints = 1
            break
        elif hints == "N" or hints == "n":
            hints = 0
            break
        else:
            print()
            print("Please enter Y or N.")
            continue

def print_board(board):
    header = " "
    for i in range(1,9):
        header += " " + str(i)
    print(header.center(width)) 

    for i in range(1,9):
        print((str(i) + " " + " ".join(board[i - 1])).center(width))

def clear_past_available_moves(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "#":
                board[i][j] = "-"

def available_moves(opp_player,player):
    for i in range(8):
        for j in range(7):
            if board[i][j] == opp_player and board[i][j + 1] == "-":
                for k in range(8):
                    count1 = 0
                    if board[i][k] == player:
                        if j > k:
                            if j - k == 1:
                                board[i][j + 1] = "#"
                            else:
                                for t in range(1,j - k):
                                    if board[i][k + t] == opp_player:
                                        count1 += 1
                                    if count1 == j - k - 1:
                                        board[i][j + 1] = "#"
    for i in range(8):
        for j in range(1,8):
            if board[i][j] == opp_player and board[i][j - 1] == "-":
                for k in range(8):
                    count2 = 0
                    if board[i][k] == player:
                        if k > j:
                            if k - j == 1:
                                board[i][j - 1] = "#"
                            else:
                                for t in range(1,k - j):
                                    if board[i][k - t] == opp_player:
                                        count2 += 1
                                    if count2 == k - j - 1:
                                        board[i][j - 1] = "#"
    for i in range(7):
        for j in range(8):
            if board[i][j] == opp_player and board[i + 1][j] == "-":
                for k in range(8):
                    count3 = 0
                    if board[k][j] == player:
                        if i > k:
                            if i - k == 1:
                                board[i + 1][j] = "#"
                            else:
                                for t in range(1,i - k):
                                    if board[k + t][j] == opp_player:
                                        count3 += 1
                                    if count3 == i - k - 1:
                                        board[i + 1][j] = "#"
    for i in range(1,8):
        for j in range(8):
            if board[i][j] == opp_player and board[i - 1][j] == "-":
                for k in range(8):
                    count4 = 0
                    if board[k][j] == player:
                        if k > i:
                            if k - i == 1:
                                board[i - 1][j] = "#"
                            else:
                                for t in range(1,k - i):
                                    if board[k - t][j] == opp_player:
                                        count4 += 1
                                    if count4 == k - i - 1:
                                        board[i - 1][j] = "#"
    for i in range(1,7):
        for j in range(1,7):
            if board[i][j] == opp_player and board[i + 1][j + 1] == "-":
                if i < j:
                    for k in range(1,i + 1):
                        count5 = 0
                        if board[i - k][j - k] == player:
                            if k == 1:
                                board[i + 1][j + 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i - t][j - t] == opp_player:
                                        count5 += 1
                                    if count5 == k - 1:
                                        board[i + 1][j + 1] = "#"
                if i >= j:
                    for k in range(1,j + 1):
                        count6 = 0
                        if board[i - k][j - k] == player:
                            if k == 1:
                                board[i + 1][j + 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i - t][j - t] == opp_player:
                                        count6 += 1
                                    if count6 == k - 1:
                                        board[i + 1][j + 1] = "#"
    for i in range(1,7):
        for j in range(1,7):
            if board[i][j] == opp_player and board[i - 1][j - 1] == "-":
                if i < j:
                    for k in range(1,8 - j):
                        count7 = 0
                        if board[i + k][j + k] == player:
                            if k == 1:
                                board[i - 1][j - 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i + t][j + t] == opp_player:
                                        count7 += 1
                                    if count7 == k - 1:
                                        board[i - 1][j - 1] = "#"
                if i >= j:
                    for k in range(1,8 - i):
                        count8 = 0
                        if board[i + k][j + k] == player:
                            if k == 1:
                                board[i - 1][j - 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i + t][j + t] == opp_player:
                                        count8 += 1
                                    if count8 == k - 1:
                                        board[i - 1][j - 1] = "#"
    for i in range(1,7):
        for j in range(1,7):
            if board[i][j] == opp_player and board[i - 1][j + 1] == "-":
                if 7 - i < j:
                    for k in range(1,8 - i):
                        count9 = 0
                        if board[i + k][j - k] == player:
                            if k == 1:
                                board[i - 1][j + 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i + t][j - t] == opp_player:
                                        count9 += 1
                                    if count9 == k - 1:
                                        board[i - 1][j + 1] = "#"
                if 7 - i >= j:
                    for k in range(1,j + 1):
                        count10 = 0
                        if board[i + k][j - k] == player:
                            if k == 1:
                                board[i - 1][j + 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i + t][j - t] == opp_player:
                                        count10 += 1
                                    if count10 == k - 1:
                                        board[i - 1][j + 1] = "#"
    for i in range(1,7):
        for j in range(1,7):
            if board[i][j] == opp_player and board[i + 1][j - 1] == "-":
                if 7 - i < j:
                    for k in range(1,8 - j):
                        count11 = 0
                        if board[i - k][j + k] == player:
                            if k == 1:
                                board[i + 1][j - 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i - t][j + t] == opp_player:
                                        count11 += 1
                                    if count11 == k - 1:
                                        board[i + 1][j - 1] = "#"
                if 7 - i >= j:
                    for k in range(1,i + 1):
                        count12 = 0
                        if board[i - k][j + k] == player:
                            if k == 1:
                                board[i + 1][j - 1] = "#"
                            else:
                                for t in range(1,k):
                                    if board[i - t][j + t] == opp_player:
                                        count12 += 1
                                    if count12 == k - 1:
                                        board[i + 1][j - 1] = "#"
    global possible_moves
    possible_moves = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "#":
                possible_moves += 1
    #print("There are " + str(possible_moves) + " possible moves")
    return possible_moves

def any_possible_moves():
    clear_past_available_moves(board)
    store1 = available_moves("X","O")
    clear_past_available_moves(board)
    store2 = available_moves("O","X")
    if store1 + store2 == 0:
        return 0

def place_piece(player):
    check = 0
    while check == 0:
        global piece_row
        global piece_column
        count = 0
        while count == 0:
            print()
            piece_row = input("Player " + player + ", choose a row in which to place your piece: ")
            if piece_row.isnumeric() == True:
                piece_row = int(piece_row)
                if piece_row <= 8 and piece_row >= 1:
                    piece_row = piece_row - 1
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
            piece_column = input("Player " + player + ", choose a column in which to place your piece: ")
            if piece_column.isnumeric() == True:
                piece_column = int(piece_column)
                if piece_column <= 8 and piece_column >= 1:
                    piece_column = piece_column - 1
                    count += 1
                else:
                    print()
                    print("Please enter an integer between 1 and 8.")
            else:
                print()
                print("Please enter an integer between 1 and 8.")
        if board[piece_row][piece_column] == "#":
            board[piece_row][piece_column] = player
            check += 1
        else:
            print()
            print("That is not a valid move. Please go again.")

def change_pieces(opp_player,player):
    global piece_row
    global piece_column
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    for i in range(1,7 - piece_column):
        if board[piece_row][piece_column + i] == opp_player and board[piece_row][piece_column + i + 1] == player:
            if i == 1:
                board[piece_row][piece_column + i] = player
            else:
                for j in range(1,i):
                    if board[piece_row][piece_column + i - j] == opp_player:
                        count1 += 1
                    if count1 == i - 1:
                        for k in range(1,i + 1):
                            board[piece_row][piece_column + k] = player
            break
    for i in range(1,7 - piece_row):
        if board[piece_row + i][piece_column] == opp_player and board[piece_row + i + 1][piece_column] == player:
            if i == 1:
                board[piece_row + i][piece_column] = player
            else:
                for j in range(1,i):
                    if board[piece_row + i - j][piece_column] == opp_player:
                        count2 += 1
                    if count2 == i - 1:
                        for k in range(1,i + 1):
                            board[piece_row + k][piece_column] = player
            break
    for i in range(1,piece_column):
        if board[piece_row][piece_column - i] == opp_player and board[piece_row][piece_column - i - 1] == player:
            if i == 1:
                board[piece_row][piece_column - i] = player
            else:
                for j in range(1,i):
                    if board[piece_row][piece_column - i + j] == opp_player:
                        count3 += 1
                    if count3 == i - 1:
                        for k in range(1,i + 1):
                            board[piece_row][piece_column - k] = player
            break
    for i in range(1,piece_row):
        if board[piece_row - i][piece_column] == opp_player and board[piece_row - i - 1][piece_column] == player:
            if i == 1:
                board[piece_row - i][piece_column] = player
            else:
                for j in range(1,i):
                    if board[piece_row - i + j][piece_column] == opp_player:
                        count4 += 1
                    if count4 == i - 1:
                        for k in range(1,i + 1):
                            board[piece_row - k][piece_column] = player
            break
    if piece_row + piece_column >= 7:
        for i in range(1,7 - piece_column):
            if board[piece_row - i][piece_column + i] == opp_player and board[piece_row - i - 1][piece_column + i + 1] == player:
                if i == 1:
                    board[piece_row - i][piece_column + i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row - i + j][piece_column + i - j] == opp_player:
                            count5 += 1
                        if count5 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row - k][piece_column + k] = player
                break
        for i in range(1,7 - piece_row):
            if board[piece_row + i][piece_column - i] == opp_player and board[piece_row + i + 1][piece_column - i - 1] == player:
                if i == 1:
                    board[piece_row + i][piece_column - i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row + i - j][piece_column - i + j] == opp_player:
                            count6 += 1
                        if count6 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row + k][piece_column - k] = player
                break
    else:
        for i in range(1,piece_row):
            if board[piece_row - i][piece_column + i] == opp_player and board[piece_row - i - 1][piece_column + i + 1] == player:
                if i == 1:
                    board[piece_row - i][piece_column + i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row - i + j][piece_column + i - j] == opp_player:
                            count7 += 1
                        if count7 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row - k][piece_column + k] = player
        for i in range(1,piece_column):
            if board[piece_row + i][piece_column - i] == opp_player and board[piece_row + i + 1][piece_column - i - 1] == player:
                if i == 1:
                    board[piece_row + i][piece_column - i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row + i - j][piece_column - i + j] == opp_player:
                            count8 += 1
                        if count8 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row + k][piece_column - k] = player
                break
    if piece_row > piece_column:
        for i in range(1,7 - piece_row):
            if board[piece_row + i][piece_column + i] == opp_player and board[piece_row + i + 1][piece_column + i + 1] == player:
                if i == 1:
                    board[piece_row + i][piece_column + i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row + i - j][piece_column + i - j] == opp_player:
                            count9 += 1
                        if count9 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row + k][piece_column + k] = player
                break
        for i in range(1,piece_column):
            if board[piece_row - i][piece_column - i] == opp_player and board[piece_row - i - 1][piece_column - i - 1] == player:
                if i == 1:
                    board[piece_row - i][piece_column - i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row - i + j][piece_column - i + j] == opp_player:
                            count10 += 1
                        if count10 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row - k][piece_column - k] = player
                break
    else:
        for i in range(1,7 - piece_column):
            if board[piece_row + i][piece_column + i] == opp_player and board[piece_row + i + 1][piece_column + i + 1] == player:
                if i == 1:
                    board[piece_row + i][piece_column + i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row + i - j][piece_column + i - j] == opp_player:
                            count11 += 1
                        if count11 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row + k][piece_column + k] = player
        for i in range(1,piece_row):
            if board[piece_row - i][piece_column - i] == opp_player and board[piece_row - i - 1][piece_column - i - 1] == player:
                if i == 1:
                    board[piece_row - i][piece_column - i] = player
                else:
                    for j in range(1,i):
                        if board[piece_row - i + j][piece_column - i + j] == opp_player:
                            count12 += 1
                        if count12 == i - 1:
                            for k in range(1,i + 1):
                                board[piece_row - k][piece_column - k] = player
                break
                
def check_board(board):
    global turn
    Xcount = 0
    Ocount = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "X":
                Xcount += 1
            elif board[i][j] == "O":
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
        yn_tracker = 0
        while yn_tracker == 0:
            print()
            yn = input("Would you like to play again? Please enter Y or N. ")
            if len(yn) != 1:
                print()
                print("Please enter Y or N.")
            elif yn == "Y" or yn =="y":
                for x in range(8):
                    for y in range(8):
                        board[x][y] = "-"
                board[3][3] = "X"
                board[3][4] = "O"
                board[4][3] = "O"
                board[4][4] = "X"
                turn = 1
                yn_tracker = 1
            elif yn =="N" or yn =="n":
                turn  = 0
                print()
                print("Goodbye!")
                yn_tracker = 1
            else:
                print()
                print("Please enter Y or N.")

def move(player):
    global turn
    global possible_moves
    if player == "X":
        opp_player = "O"
    else:
        opp_player = "X"
    clear_past_available_moves(board)
    if hints == 1:
        available_moves(opp_player,player)
        print()
        print_board(board)
    if hints == 0:
        print()
        print_board(board)
        available_moves(opp_player,player)
    if possible_moves != 0:
        place_piece(player)
        change_pieces(opp_player,player)
    else:
        print()
        print("Player " + player + " has no possible moves.")
    turn += 1
           
while turn > 0:
    if any_possible_moves() == 0:
        print()
        print_board(board)
        print()
        print("No moves left!")
        check_board(board)
    if turn == 1:
        ask_hints()
    if turn % 2 != 0:
        move("X")
    else:
        move("O")
