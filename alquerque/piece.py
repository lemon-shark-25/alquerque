import pygame
from .constants import POSITION_SIZE, WHITE, BLACK, GRAY

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.size_coef = 0.25
        self.border = 4
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = POSITION_SIZE * self.col + POSITION_SIZE//2
        self.y = POSITION_SIZE * self.row + POSITION_SIZE//2

    def draw(self, win):
        pygame.draw.circle(win, GRAY, (self.x, self.y), POSITION_SIZE*self.size_coef)
        pygame.draw.circle(win, self.color, (self.x, self.y), POSITION_SIZE*self.size_coef - self.border)
