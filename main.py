import pygame
import sys

from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board


def get_mouse_pos(mouseX, mouseY):
    col = int(mouseX // SQUARE_SIZE)
    row = int(mouseY // SQUARE_SIZE)

    return row, col


if __name__ == '__main__':
    # PyGame initialization
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')

    # Board initialization
    board = Board(window)
    board.draw_lines()

    # Game over variable
    game_over = False

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row, clicked_col = get_mouse_pos(mouseX, mouseY)

                if board.available_square(clicked_row, clicked_col):
                    board.mark_square(clicked_row, clicked_col, board.player)
                    if board.check_win():
                        game_over = True
                    board.player = board.player % 2 + 1

                    board.draw_figures()

            # Press 'R' to restart the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.restart_game()
                    game_over = False

            # Press 'Q' to exit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.update()
