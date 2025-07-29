import pygame
from alquerque import WIDTH, HEIGHT
FPS = 60

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alquerque")

def main():
    running = True
    clock = pygame.time.Clock

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

main()

