#!/bin/python3
import os
import contextlib
import Game
#this is done to suppress the pygame output when loaded.
with contextlib.redirect_stdout(None):
    import pygame


def update_board_graphic():
    for row in range(8):
        for column in range(8):
            if game.board[row][column] == "O":
                pygame.draw.rect(display, white, (column*32, row*32, 32, 32))
            elif game.board[row][column] == "#":
                pygame.draw.rect(display, red, (column*32, row*32, 32, 32))
            elif game.board[row][column] == "X":
                pygame.draw.rect(display, black, (column*32, row*32, 32, 32))

#Program Driver
if __name__ == "__main__":
    
    #Create the Game object using the Game constructor / __init__ method.
    game = Game.Game()

    #initialize pygame
    pygame.init()

    #tile colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    #create specifications for the display window
    window_dimensions = (256, 256)
    display = pygame.display.set_mode((window_dimensions))
    display.fill(green)
    pygame.display.set_caption("Othello")

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

    while game.turn > 0:
        update_board_graphic()
        pygame.display.flip()
        if game.any_possible_moves() == 0:
            print()
            game.print_board()
            print()
            print("No moves left!")
            game.check_board(game.board)
        if game.turn == 1:
            game.ask_hints()
        if game.turn % 2 != 0:
            game.move("X")
        else:
            game.move("O")

    pygame.quit()
