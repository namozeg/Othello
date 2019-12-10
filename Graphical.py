import contextlib
from Othello import board
#this is done to suppress the pygame output when loaded.
with contextlib.redirect_stdout(None):
    import pygame

#initialize pygame
pygame.init()

#tile colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

#create specifications for the display window
window_dimensions = (256, 256)
pygame.display.set_mode((window_dimensions))
pygame.display.set_caption("Othello")

def update_board():
    for row in range(9):
        for column in range(9):
            if board[row][column] == "X":
                pass
            elif board[row][column] == "O":
                pass
            else:
                pass

def display_board():
    pygame.display.flip()

def close():
    pygame.quit()
