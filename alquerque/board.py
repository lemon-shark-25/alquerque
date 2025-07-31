import pygame
from .constants import ROWS, COLS, POSITION_SIZE, BLACK, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.black_left = 12
        self.white_left = 12
        self.create_board() 

    def draw_board(self, win):
        line_weight = 10
        win.fill(WHITE)

        def pos(row, col):
           return (POSITION_SIZE * row + POSITION_SIZE // 2,
                   POSITION_SIZE * col + POSITION_SIZE // 2)

        # Dibujar puntos de intersección
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.circle(win, BLACK, pos(row, col), POSITION_SIZE // 5)

        # Dibujar líneas horizontales y verticales
        for i in range(ROWS):
            # Horizontal
            pygame.draw.line(win, BLACK, pos(0, i), pos(4, i), line_weight)
            # Vertical
            pygame.draw.line(win, BLACK, pos(i, 0), pos(i, 4), line_weight)

        # Diagonal principal descendente (↘)
        pygame.draw.line(win, BLACK, pos(0, 0), pos(4, 4), line_weight)
        # Diagonal principal ascendente (↗)
        pygame.draw.line(win, BLACK, pos(0, 4), pos(4, 0), line_weight)

        # Diagonales secundarias descendentes (↘)
        pygame.draw.line(win, BLACK, pos(0, 2), pos(2, 4), line_weight)
        pygame.draw.line(win, BLACK, pos(2, 0), pos(4, 2), line_weight)

        # Diagonales secundarias ascendentes (↗)
        pygame.draw.line(win, BLACK, pos(0, 2), pos(2, 0), line_weight)
        pygame.draw.line(win, BLACK, pos(2, 4), pos(4, 2), line_weight)

    def create_board(self):
       for row in range(5):
        self.board.append([])
        for col in range(5):
            if row < 2:  # Las dos primeras filas: piezas blancas
                self.board[row].append(Piece(row, col, WHITE))
            elif row > 2:  # Las dos últimas filas: piezas negras
                self.board[row].append(Piece(row, col, BLACK))
            elif row == 2:
                if col < 2:  # Parte izquierda de la fila del medio: blancas
                    self.board[row].append(Piece(row, col, WHITE))
                elif col > 2:  # Parte derecha: negras
                    self.board[row].append(Piece(row, col, BLACK))
                else:  # Centro exacto (2,2): vacío
                    self.board[row].append(None)

    def get_piece(self, row, col):
        return self.board[row][col]
        
    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece is not None:
                    piece.draw(win)
