# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import pause, crea_boutons_pause, ca_clique, gameover, crea_boutons_gameover, home, crea_boutons_home, parametrage, crea_boutons_parametrage

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("test")

    # dictionnaire contetant les touches par defaut pour les mouvements haut bas gauche droite

    dicocle = {
        "up": pygame.K_z,
        "down": pygame.K_s,
        "left": pygame.K_q,
        "right": pygame.K_d
    }

    clock = pygame.time.Clock()
    game = Game(dicocle)

    # variables pour gerer les etats du jeu

    ppause = False      # jeu en pause
    estmort = False     # je joueur a perdu
    running = True      # execution du jeu (si false la fenetre s'eteint)
    hhome = True        # menu principal
    param = False       # menu parametre

    changementdecle = None  # l'utilisateur est il en train de changer une touche

    # initialisation des boutons des differents menus

    les_boutons_pause = crea_boutons_pause()
    les_boutons_gameover = crea_boutons_gameover()
    les_boutons_home = crea_boutons_home()
    les_boutons_param = crea_boutons_parametrage(dicocle)
    
    while running:
        dt = clock.tick(FPS) / 1000 #conversion en s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # gestion des touches

            if event.type == pygame.KEYDOWN:

                # faut les touches soient assignees

                if changementdecle :
                    dicocle[changementdecle] = event.key                    # on assigne
                    changementdecle = None                                  # on a fini le chnagement
                    les_boutons_param = crea_boutons_parametrage(dicocle)   # on met a jour les touches du menu param 
                    continue

                # quiiter le jeu
                if event.key == pygame.K_ESCAPE:
                    running = False

                # afficher le menu pause
                if event.key == pygame.K_p:
                    ppause = True
                
                # relancer la partie
                if event.key == pygame.K_r:
                    game = Game(dicocle)
                
                # aller sur le menu principal (abandon de la game)
                if event.key == pygame.K_m:
                    hhome = True

            # gestion boutons selon les etats du jeu

            # si on est dans le menu parametre et qu'on n'est pas en train de changeer les touches

            if param and not changementdecle:

                action = ca_clique(event, les_boutons_param)

                if action == "qparam": # qparam pour quitter le menu parametre
                    param = False
                
                elif action and action.startswith("bind_"):
                    changementdecle = action.split("_")[1]

            # si on est dans le menu principal
            
            elif hhome:

                action = ca_clique(event, les_boutons_home)

                if action == "start":           # on lance la parti et on quite le menu principal
                    game = Game(dicocle)
                    hhome = False
                
                elif action == "quit":          # on arrete le jeu, la fenetre se coupe
                    running = False

                elif action == "parametres":    # on affiche le menu parametre
                    param = True

            # si on est dans le menu pause

            elif ppause:

                action = ca_clique(event, les_boutons_pause)

                if action == "home":            # on va dans le menu principal donc on quite le menu pause et on abandonne la partie
                    hhome = True
                    ppause = False

                if action == "resume":          # la partie n'est plus en pause et le menu pause disparait
                    ppause = False

                elif action == "restart":       # on n'est plus en pause et on relance une game a zero
                    game = Game(dicocle)
                    ppause = False

                elif action == "parametres":    # affichage du menu parametre
                    param = True 

                elif action == "quit":          # on arrete le jeu, la fenetre se coupe
                    running = False
            
            # si l'utilisateur a perdu
            
            elif estmort:

                action = ca_clique(event, les_boutons_gameover)

                if action == "home":            # on va dans le menu principal donc on quite le menu gameover 
                    hhome = True                # variable pour activer l'affichage du menu principal
                    estmort = False             # variable pour activer l'affichage du menu gameover

                elif action == "restart":       # on relance une game a zero
                    game = Game(dicocle)
                    estmort = False             # variable pour activer l'affichage du menu gameover

                elif action == "parametres":    
                    param = True                # variable pour activer l'affichage du menu parametre

                elif action == "quit":          # on arrete le jeu, la fenetre se coupe
                    running = False
                 
        # gestion du bordel

        # gestion de la mort (si les hp atteingne 0)

        if game.player.health <= 0 :
            estmort = True

        # si on est pas en pause, ni mort ni dans le menu home ni ans le menu parametre alors on update

        if not ppause and not estmort and not hhome and not param:
            game.update(dt)
        
        # si on est pas dans le menu principal alors on dessine

        if not hhome:
            game.draw(screen)

        if hhome:
            screen.fill((20,20,20))         # fond noir
            home(screen, les_boutons_home)  #
        elif estmort:
            gameover(screen, les_boutons_gameover)                      # affichage du menu gameover
        elif ppause:
            pause(screen, les_boutons_pause)
        if param:
            parametrage(screen, les_boutons_param, changementdecle)


        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
