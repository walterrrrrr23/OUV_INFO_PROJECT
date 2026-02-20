# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import pause, crea_boutons, ca_clique

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("test")

    clock = pygame.time.Clock()
    game = Game()

    ppause = False
    running = True
    les_boutons = crea_boutons()
    
    while running:
        dt = clock.tick(FPS) / 1000 #conversion en s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # gestion des touches

            if event.type == pygame.KEYDOWN:

                # quiiter le jeu
                if event.key == pygame.K_ESCAPE:
                    running = False

                # afficher le menu pause
                if event.key == pygame.K_p:
                    ppause = not ppause

            # gestion souris

            if ppause:
                action = ca_clique(event, les_boutons)
                if action == "resume":
                    ppause = False

                elif action == "restart":
                    game = Game() 
                    ppause = False

                elif action == "quit":
                    running = False
            
        # si on est en pause, on affiche le menu
        if ppause :
            game.draw(screen)
            pause(screen, les_boutons)
        
        # si on est pas en pause, on update
        else:
            game.update(dt)
            game.draw(screen)
        
        # gestion du gameover

            if game.player.health <= 0 :
                running = False #METTRE LOGIQUE GAME_OVER

        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
