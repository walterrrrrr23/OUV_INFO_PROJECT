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
    game = Game()
    ppause = False

    running = True
    while running:
        dt = clock.tick(FPS) / 1000 #conversion en s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if game.player.health <= 0 :
                running = False #METTRE LOGIQUE GAME_OVER

            if event.type == pygame.KEYDOWN:

                # quiiter le jeu
                if event.key == pygame.K_ESCAPE:
                    running = False

                # afficher le menu pause
                if event.key == pygame.K_p:
                    ppause = not ppause
            
        # si on est en pause, on affiche le menu
        if ppause :
            game.draw(screen)
            pause(screen)
        
        # si on est pas en pause, on update
        else:
            game.update(dt)
            game.draw(screen)

        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
