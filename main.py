# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import pause

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("test")

    clock = pygame.time.Clock()
    game = Game(screen)
    ppause = False

    running = True
    while running:
        dt = clock.tick(FPS) / 1000 #conversion en s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()

        if key_pressed[pygame.K_p]:
            ppause = not ppause
        
        if ppause:
            print("hell yeah")
            pause()

        else :
            print("hell no")

        game.update(dt)
        game.draw()

        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
