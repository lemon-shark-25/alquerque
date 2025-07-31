import pygame
from alquerque import WIDTH, HEIGHT
from alquerque.board import Board

# Local constants
FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alquerque")

def main():
    running = True
    clock = pygame.time.Clock()

    board = Board()
    board.create_board()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rendering
        board.draw(WIN)

        pygame.display.flip()

    pygame.quit()

main()

