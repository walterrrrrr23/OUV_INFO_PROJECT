# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
from game import Game
from menu_pause import pause, crea_boutons_pause, ca_clique, gameover, crea_boutons_gameover, home, crea_boutons_home, parametrage, crea_boutons_parametrage, credits, crea_boutons_credits, amelio, crea_boutons_amelio
from player import Player

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
    cred = False        # menu credits

    changementdecle = None  # l'utilisateur est il en train de changer une touche

    # initialisation des boutons des differents menus

    les_boutons_pause = crea_boutons_pause()
    les_boutons_gameover = crea_boutons_gameover()
    les_boutons_home = crea_boutons_home()
    les_boutons_cred = crea_boutons_credits()
    les_boutons_amelio = crea_boutons_amelio()
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

                # mettre en pause
                if event.key == pygame.K_ESCAPE:
                    ppause = True

                # afficher le menu pause
                if event.key == pygame.K_n:
                    running = False               # variable pour activer l'affichage du menu pause
                
                # relancer la partie
                if event.key == pygame.K_r:
                    game = Game(dicocle)
                
                # aller sur le menu principal (abandon de la game)
                if event.key == pygame.K_m:
                    hhome = True                # variable pour activer l'affichage du menu principal

            # gestion boutons selon les etats du jeu

            # si on est dans le menu parametre et qu'on n'est pas en train de changeer les touches

            if param and not changementdecle:

                action = ca_clique(event, les_boutons_param)

                if action == "qparam": # qparam pour quitter le menu parametre
                    param = False
                
                elif action and action.startswith("bind_"):
            
                    changementdecle = action.split("_")[1]
            
            elif cred:
                action = ca_clique(event, les_boutons_cred)

                if action == "qcredits": # qcredits pour quitter le menu credits
                    cred = False

            # si on est dans le menu principal
            
            elif hhome:

                action = ca_clique(event, les_boutons_home)

                if action == "start":           # on lance la parti et on quite le menu principal
                    game = Game(dicocle)
                    hhome = False               # variable pour activer l'affichage du menu principal
                
                elif action == "quit":          # on arrete le jeu, la fenetre se coupe
                    running = False

                elif action == "parametres":
                    param = True                # variable pour activer l'affichage du menu parametre

                elif action == "credits":
                    cred = True                # variable pour activer l'affichage du menu parametre

            # si on est dans le menu pause

            elif ppause:

                action = ca_clique(event, les_boutons_pause)

                if action == "home":            # on va dans le menu principal donc on quite le menu pause et on abandonne la partie
                    hhome = True                # variable pour activer l'affichage du menu principal
                    ppause = False              # variable pour activer l'affichage du menu pause

                if action == "resume":          # la partie n'est plus en pause et le menu pause disparait
                    ppause = False              # variable pour activer l'affichage du menu pause

                elif action == "restart":       # on n'est plus en pause et on relance une game a zero
                    game = Game(dicocle)
                    ppause = False              # variable pour activer l'affichage du menu pause

                elif action == "parametres":    # affichage du menu parametre
                    param = True 

                elif action == "quit":          # on arrete le jeu, la fenetre se coupe
                    running = False
            
            # si il choisi son amelio

            elif game.player.amelio_en_cours:
                
                action = ca_clique(event, les_boutons_amelio)

                for b in les_boutons_amelio:
                    if action == b["action"]:
                        if game.player.coin >= b["prix"]:
                            game.player.coin -= b["prix"]

                            if action == "augmente_vie":

                                game.player.max_health += 10                    # on augmente le maxi de PV
                                game.player.health = game.player.max_health     # vu qu'on soigne a chaque monter en niveau, on set les PV au max
                                game.player.amelio_en_cours = False             # il a fini de choisir son amelio
                            
                            elif action == "augmente_vitesse":

                                game.player.speed += 50
                                game.player.amelio_en_cours = False
            
                if action == "resume":          # la partie n'est plus en pause et le menu pause disparait
                    game.player.amelio_en_cours = False              # variable pour activer l'affichage du menu pause

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

        if not ppause and not estmort and not hhome and not param and not cred and not game.player.amelio_en_cours:
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
        elif game.player.amelio_en_cours:
            amelio(screen, les_boutons_amelio, game.player)
        if cred:
            credits(screen, les_boutons_cred)
        if param:
            parametrage(screen, les_boutons_param, changementdecle)


        pygame.display.flip() #screen update

    pygame.quit()

if __name__ == "__main__":
    main()
