# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game import Game

def main():
    print("test")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("test")

    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update(dt)
        game.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
