import pygame
import sys

from constants import WIDTH, HEIGHT, BG_COLOR, LINE_WIDTH, LINE_COLOR, BOARD_COLS, BOARD_ROWS, TILE_WIDTH, TILE_HEIGHT
from board import Board


def get_mouse_pos(x, y):
    row = int(y // 200)
    col = int(x // 200)

    return row, col


if __name__ == '__main__':
    # PyGame initialization
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TicTacToe')

    # Board initialization
    board = Board(window)
    board.draw_lines()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row, clicked_col = get_mouse_pos(mouseX, mouseY)

                if board.available_square(clicked_row, clicked_col):
                    if board.player == 1:
                        board.mark_square(clicked_row, clicked_col, board.player)
                        board.player = 2
                    elif board.player == 2:
                        board.mark_square(clicked_row, clicked_col, board.player)
                        board.player = 1

                    board.draw_figures()
                    board.check_win()

                board.print_console_board()

        pygame.display.update()
