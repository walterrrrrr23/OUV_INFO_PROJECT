# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import pause, crea_boutons_pause, ca_clique, gameover, crea_boutons_gameover

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("test")

    clock = pygame.time.Clock()
    game = Game()

    ppause = False
    estmort = False
    running = True
    les_boutons_pause = crea_boutons_pause()
    les_boutons_gameover = crea_boutons_gameover()
    
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

            if ppause or estmort:

                action = ca_clique(event, les_boutons_pause)

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
            pause(screen, les_boutons_pause)
        
        # si on est pas en pause, on update
        else:
            game.update(dt)
            game.draw(screen)
        
        # gestion du gameover

            if game.player.health <= 0 :
                estmort = not estmort
                gameover(screen, les_boutons_gameover)
                #running = False #METTRE LOGIQUE GAME_OVER

        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
