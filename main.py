# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import Pause

def main():
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
            
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_p]:
            PAUSE = not PAUSE
            print(Pause)


        game.update(dt)
        game.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
