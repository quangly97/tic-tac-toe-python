import numpy as np
import pygame
import math
from math import pi

LENGTH = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def create_board():
    return np.zeros((LENGTH, LENGTH))

def draw_board(screen, board):
    for row in range(LENGTH):
        for col in range(LENGTH):
            pygame.draw.rect(screen, BLACK, (row*PXLSIZE, col*PXLSIZE, PXLSIZE, PXLSIZE))

    for row in range(LENGTH):
        for col in range(LENGTH):
            if(board[row][col] == 1):
                pygame.draw.line(screen, WHITE, (col*PXLSIZE, row*PXLSIZE), (col*PXLSIZE + PXLSIZE, row*PXLSIZE + PXLSIZE), 5)
                pygame.draw.line(screen, WHITE, (col*PXLSIZE + PXLSIZE, row*PXLSIZE), (col*PXLSIZE, row*PXLSIZE + PXLSIZE), 5)
            elif(board[row][col] == 2):
                pygame.draw.arc(screen, WHITE, (col*PXLSIZE + 5, row*PXLSIZE + 5, PXLSIZE - 10, PXLSIZE - 10), 0, 2*pi, 5)

    pygame.draw.line(screen, WHITE, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, WHITE, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, WHITE, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, WHITE, (0, 200), (300, 200), 5)

def insert_piece(board, piece, position):
    board[position[1]][position[0]] = piece

def spot_available(board, position):
    return board[position[1]][position[0]] == 0

def board_full(board):
    for row in range(LENGTH):
        for col in range(LENGTH):
            if board[row][col] == 0:
                return False
    return True

def tic_tac_toe(board, piece):
    if (board[0][0] == piece and board[0][1] == piece and board[0][2] == piece) or (board[1][0] == piece and board[1][1] == piece and board[1][2] == piece) or (board[2][0] == piece and board[2][1] == piece and board[2][2] == piece) or (board[0][0] == piece and board[1][0] == piece and board[2][0] == piece) or (board[0][1] == piece and board[1][1] == piece and board[2][1] == piece) or (board[0][2] == piece and board[1][2] == piece and board[2][2] == piece) or (board[0][0] == piece and board[1][1] == piece and board[2][2] == piece) or (board[0][2] == piece and board[1][1] == piece and board[2][0] == piece):
        return True

board = create_board()
PXLSIZE = 100
RADIUS = PXLSIZE//2

game_over = False
turn = 0

width = LENGTH*PXLSIZE + 5
size = (width, width)
screen = pygame.display.set_mode(size)

draw_board(screen, board)
pygame.display.update()

pygame.init()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if turn == 0:
                position = (math.floor(event.pos[0]//PXLSIZE) , math.floor(event.pos[1]//PXLSIZE))
                if spot_available(board, position):
                    insert_piece(board, 1, position)
                
                if tic_tac_toe(board, 1):
                    game_over = True
            else:
                position = (math.floor(event.pos[0]//PXLSIZE) , math.floor(event.pos[1]//PXLSIZE))
                if spot_available(board, position):
                    insert_piece(board, 2, position)
                
                if tic_tac_toe(board, 2):
                    game_over = True

            if board_full(board):
                game_over = True

            draw_board(screen, board)
            pygame.display.update()

            turn += 1
            turn = turn % 2

            if(game_over):
                pygame.time.delay(5000)
