# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import pause, crea_boutons_pause, ca_clique, gameover, crea_boutons_gameover, home, crea_boutons_home

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("test")

    clock = pygame.time.Clock()
    game = Game()

    ppause = False
    estmort = False
    running = True
    hhome = True

    les_boutons_pause = crea_boutons_pause()
    les_boutons_gameover = crea_boutons_gameover()
    les_boutons_home = crea_boutons_home()
    
    while running:
        dt = clock.tick(FPS) / 2000 #conversion en s

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
                    ppause = True

            # gestion boutons selon les etats du jeu

            if hhome:
                action = ca_clique(event, les_boutons_home)

                if action == "start":
                    game = Game()
                    hhome = False
                
                elif action == "quit":
                    running = False

            elif ppause:
                action = ca_clique(event, les_boutons_pause)

                if action == "home":
                    hhome = True
                    ppause = False

                if action == "resume":
                    ppause = False

                elif action == "restart":
                    game = Game()
                    ppause = False 

                elif action == "quit":
                    running = False
            
            elif estmort:
                action = ca_clique(event, les_boutons_gameover)

                if action == "home":
                    hhome = True
                    estmort = False

                elif action == "restart":
                    game = Game()
                    estmort = False 

                elif action == "quit":
                    running = False
                 
        # gestion du bordel

        if game.player.health <= 0 :
            estmort = True

        # si on est pas en pause, ni mortn ni dans le menu home on update
        if not ppause and not estmort and not hhome:
            game.update(dt)
        
        if not hhome:
            game.draw(screen)

        if hhome:
            screen.fill((20,20,20))
            home(screen, les_boutons_home)
        elif estmort:
            gameover(screen, les_boutons_gameover)
        elif ppause:
            pause(screen, les_boutons_pause)


        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
