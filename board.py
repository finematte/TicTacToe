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
        pygame.draw.line(self.window, constants.LINE_COLOR, (0, constants.SQUARE_SIZE), (constants.WIDTH, constants.SQUARE_SIZE), constants.LINE_WIDTH)
        pygame.draw.line(self.window, constants.LINE_COLOR, (0, 2 * constants.SQUARE_SIZE), (constants.WIDTH, 2 * constants.SQUARE_SIZE), constants.LINE_WIDTH)

        # Vertical lines
        pygame.draw.line(self.window, constants.LINE_COLOR, (constants.SQUARE_SIZE, 0), (constants.SQUARE_SIZE, constants.HEIGHT), constants.LINE_WIDTH)
        pygame.draw.line(self.window, constants.LINE_COLOR, (2 * constants.SQUARE_SIZE, 0), (2 * constants.SQUARE_SIZE, constants.HEIGHT), constants.LINE_WIDTH)

    def draw_figures(self):
        for row in range(constants.BOARD_ROWS):
            for col in range(constants.BOARD_COLS):
                if self.console_board[row][col] == 1:
                    pygame.draw.circle(self.window, constants.CIRCLE_COLOR, (int(col * constants.SQUARE_SIZE + constants.SQUARE_SIZE / 2), int(row * constants.SQUARE_SIZE + constants.SQUARE_SIZE / 2)), constants.CIRCLE_RADIUS, constants.CIRCLE_WIDTH)
                elif self.console_board[row][col] == 2:
                    pygame.draw.line(self.window, constants.CROSS_COLOR,
                                     (col * constants.SQUARE_SIZE + constants.SPACE, row * constants.SQUARE_SIZE + constants.SQUARE_SIZE - constants.SPACE),
                                     (col * constants.SQUARE_SIZE + constants.SQUARE_SIZE - constants.SPACE, row * constants.SQUARE_SIZE + constants.SPACE),
                                     constants.CROSS_WIDTH)
                    pygame.draw.line(self.window, constants.CROSS_COLOR,
                                     (col * constants.SQUARE_SIZE + constants.SPACE, row * constants.SQUARE_SIZE + constants.SPACE),
                                     (col * constants.SQUARE_SIZE + constants.SQUARE_SIZE - constants.SPACE, row * constants.SQUARE_SIZE + constants.SQUARE_SIZE - constants.SPACE),
                                     constants.CROSS_WIDTH)

    def check_win(self):
        # Vertical win check
        for col in range(constants.BOARD_COLS):
            if self.console_board[0][col] == self.player and self.console_board[1][col] == self.player and self.console_board[2][col] == self.player:
                self.draw_vertical_line(col, self.player)
                return True

        # Horizontal win check
        for row in range(constants.BOARD_ROWS):
            if self.console_board[row][0] == self.player and self.console_board[row][1] == self.player and self.console_board[row][2] == self.player:
                self.draw_horizontal_line(row, self.player)
                return True

        # Ascending diagonal win check
        if self.console_board[2][0] == self.player and self.console_board[1][1] == self.player and self.console_board[0][2] == self.player:
            self.draw_asc_diagonal(self.player)
            return True

        # Descending diagonal win check
        if self.console_board[0][0] == self.player and self.console_board[1][1] == self.player and self.console_board[2][2] == self.player:
            self.draw_desc_diagonal(self.player)
            return True

        return False

    def draw_vertical_line(self, col, player):
        posX = col * constants.SQUARE_SIZE + constants.SQUARE_SIZE / 2

        if self.player == 1:
            color = constants.CIRCLE_COLOR
        elif player == 2:
            color = constants.CROSS_COLOR

        pygame.draw.line(self.window, color, (posX, 15), (posX, constants.HEIGHT - 15), constants.WIN_LINE_WIDTH)

    def draw_horizontal_line(self, row, player):
        posY = row * constants.SQUARE_SIZE + constants.SQUARE_SIZE / 2

        if self.player == 1:
            color = constants.CIRCLE_COLOR
        elif player == 2:
            color = constants.CROSS_COLOR

        pygame.draw.line(self.window, color, (15, posY), (constants.WIDTH - 15, posY), constants.WIN_LINE_WIDTH)

    def draw_asc_diagonal(self, player):
        if self.player == 1:
            color = constants.CIRCLE_COLOR
        elif player == 2:
            color = constants.CROSS_COLOR

        pygame.draw.line(self.window, color, (15, constants.HEIGHT - 15), (constants.WIDTH - 15, 15), constants.WIN_LINE_WIDTH)

    def draw_desc_diagonal(self, player):
        if self.player == 1:
            color = constants.CIRCLE_COLOR
        elif player == 2:
            color = constants.CROSS_COLOR

        pygame.draw.line(self.window, color, (15, 15), (constants.WIDTH - 15, constants.HEIGHT - 15), constants.WIN_LINE_WIDTH)

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

    def restart_game(self):
        self.window.fill(constants.BG_COLOR)
        self.draw_lines()
        self.player = 1

        for row in range(constants.BOARD_ROWS):
            for col in range(constants.BOARD_COLS):
                self.console_board[row][col] = 0