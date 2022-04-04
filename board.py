import pygame
import constants
import numpy as np


class Board:
    def __init__(self, window):
        self.console_board = np.zeros((constants.BOARD_ROWS, constants.BOARD_COLS))
        self.window = window
        self.player = 1

        self.window.fill(constants.BG_COLOR)

    def draw_lines(self):
        # Horizontal lines
        pygame.draw.line(self.window, constants.LINE_COLOR, (0, 200), (600, 200), constants.LINE_WIDTH)
        pygame.draw.line(self.window, constants.LINE_COLOR, (0, 400), (600, 400), constants.LINE_WIDTH)

        # Vertical lines
        pygame.draw.line(self.window, constants.LINE_COLOR, (200, 0), (200, 600), constants.LINE_WIDTH)
        pygame.draw.line(self.window, constants.LINE_COLOR, (400, 0), (400, 600), constants.LINE_WIDTH)

    def draw_figures(self):
        for row in range(constants.BOARD_ROWS):
            for col in range(constants.BOARD_COLS):
                if self.console_board[row][col] == 1:
                    pygame.draw.circle(self.window, constants.CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), constants.CIRCLE_RADIUS, constants.CIRCLE_WIDTH)
                elif self.console_board[row][col] == 2:
                    pygame.draw.line(self.window, constants.CROSS_COLOR,
                                     (col * 200 + constants.SPACE, row * 200 + 200 - constants.SPACE),
                                     (col * 200 + 200 - constants.SPACE, row * 200 + constants.SPACE),
                                     constants.CROSS_WIDTH)
                    pygame.draw.line(self.window, constants.CROSS_COLOR,
                                     (col * 200 + constants.SPACE, row * 200 + constants.SPACE),
                                     (col * 200 + 200 - constants.SPACE, row * 200 + 200 - constants.SPACE),
                                     constants.CROSS_WIDTH)

    def check_win(self):
        pass

    def mark_square(self, row, col, player):
        self.console_board[row][col] = player

    def available_square(self, row, col):
        return self.console_board[row][col] == 0

    def is_board_full(self):
        for row in range(constants.BOARD_ROWS):
            for col in range(constants.BOARD_COLS):
                if self.console_board[row][col] == 0:
                    return False

        return True

    def print_console_board(self):
        print(self.console_board)
