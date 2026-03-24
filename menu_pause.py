import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY


def HealthBar(player, display):

    bar_lenght_pixel = SCREEN_WIDTH//4 + 100
    health = player.health
    maxhealth = player.max_health
    offsetx = 240
    offsety = 200
    sizex = health/maxhealth*bar_lenght_pixel
    sizey = 35

    #bar de fond
    pygame.draw.rect(display, pygame.Color(0,0,0), (offsetx, offsety, bar_lenght_pixel, sizey))
    #bar rouge
    pygame.draw.rect(display, pygame.Color(255,0,0), (offsetx, offsety, sizex, sizey))

    
    police_du_texte = pygame.font.Font("assets/fonts/Pix32.ttf", 20)
    info1_surface = police_du_texte.render(f"{health} / {maxhealth}", True, (200, 200, 200))

    info_rect = info1_surface.get_rect(center=(bar_lenght_pixel//2 + offsetx, sizey//2 + offsety))

    display.blit(info1_surface, info_rect)

    sheet = pygame.image.load("assets/sprites/coin_sheet.png").convert_alpha()
    coin = sheet.subsurface(pygame.Rect(0*TAILLE_SPRITE, 0*TAILLE_SPRITE, 64, 64))
    coin = pygame.transform.scale(coin, (64*ZOOM*1.5, 64*ZOOM*1.5))

    rect = pygame.Rect((0,0), (10,10))
    rect.center = (offsetx-90, offsety + 15)
    display.blit(coin, rect)

    info1_surface = police_du_texte.render(f"{player.coin}", True, (200, 200, 200))

    info_rect = info1_surface.get_rect(center=(offsetx+60, offsety+120))

    display.blit(info1_surface, info_rect)


def home(screen, boutons):

    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(150)     # 0 transparant -> 255 opaque
    floutage.fill((0,0,0))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    police_du_titre = pygame.font.Font("assets/fonts/Pix32.ttf", 50)

    # le texte du menu pause

    titre = police_du_titre.render("HOME", True, (255, 255, 255))

    # pour center ce qu'on a ecrit

    rectangle_du_titre = titre.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    # afficher le titre

    screen.blit(titre, rectangle_du_titre)

    # gestion de la souris

    pos_souris = pygame.mouse.get_pos()

    for b in boutons :
        if b["rect"].collidepoint(pos_souris):
            color = (180, 180, 180)
            pygame.draw.rect(screen, (255, 255, 255), b["rect"].inflate(4,4), border_radius = 10, width = 2)
        else :
            color = (100, 100, 100)

        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)

  
def pause(screen, boutons):

    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(150)     # 0 transparant -> 255 opaque
    floutage.fill((0,0,0))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    police_du_titre = pygame.font.Font("assets/fonts/Pix32.ttf", 50)

    # le texte du menu pause

    titre = police_du_titre.render("PAUSE", True, (255, 255, 255))

    # pour center ce qu'on a ecrit

    rectangle_du_titre = titre.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))

    # afficher le titre

    screen.blit(titre, rectangle_du_titre)

    # gestion de la souris

    pos_souris = pygame.mouse.get_pos()

    for b in boutons :
        if b["rect"].collidepoint(pos_souris):
            color = (180, 180, 180)
            pygame.draw.rect(screen, (255, 255, 255), b["rect"].inflate(4,4), border_radius = 10, width = 2)
        else :
            color = (100, 100, 100)

        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)


def gameover(screen, boutons):

    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(150)     # 0 transparant -> 255 opaque
    floutage.fill((150,150,150))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    police_du_titre = pygame.font.Font("assets/fonts/Pix32.ttf", 50)
    #police_du_texte = pygame.font.SysFont("arial", 40)

    # le texte du menu pause

    titre = police_du_titre.render("GAMEOVER", True, (255, 0, 0))

    # pour center ce qu'on a ecrit

    rectangle_du_titre = titre.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    # afficher le titre

    screen.blit(titre, rectangle_du_titre)

    # gestion de la souris

    pos_souris = pygame.mouse.get_pos()

    for b in boutons :
        if b["rect"].collidepoint(pos_souris):
            color = (180, 180, 180)
            pygame.draw.rect(screen, (255, 255, 255), b["rect"].inflate(4,4), border_radius = 10, width = 2)
        else :
            color = (100, 100, 100)

        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)


def parametroge(screen, boutons):
    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(150)     # 0 transparant -> 255 opaque
    floutage.fill((0,0,0))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    police_du_titre = pygame.font.Font("assets/fonts/Pix32.ttf", 50)

    # le texte du menu pause

    titre = police_du_titre.render("Paramètres", True, (255, 255, 255))
    blabla1_surface = police_du_titre.render("hihiha", True, (0, 255, 255))

    # pour center ce qu'on a ecrit

    rectangle_du_titre = titre.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
    rectangle_du_titre2 = blabla1_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80 ))

    # afficher le titre

    screen.blit(titre, rectangle_du_titre)
    screen.blit(blabla1_surface, rectangle_du_titre2)

    # gestion de la souris

    pos_souris = pygame.mouse.get_pos()

    for b in boutons :
        if b["rect"].collidepoint(pos_souris):
            color = (180, 180, 180)
            pygame.draw.rect(screen, (255, 255, 255), b["rect"].inflate(4,4), border_radius = 10, width = 2)
        else :
            color = (100, 100, 100)

        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)

        
def parametrage(screen, boutons, changementdecle = None):

    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(255)
    floutage.fill((10,10,15))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    police_du_titre = pygame.font.Font("assets/fonts/Pix32.ttf", 50)
    police_du_texte = pygame.font.Font("assets/fonts/Pix32.ttf", 30)

    # le texte du menu

    titre = police_du_titre.render("Paramètres", True, (255, 255, 255))
    
    # msg si on attend une touche
    if changementdecle:
        #le msg
        msg = f"Appuyez sur la nouvelle touche pour : {changementdecle.upper()}"
        #la couleur du msg
        color = (255, 255, 0)
    else:
        #le msg
        msg = "Cliquez sur une action pour modifier"
        #la couleur du msg
        color = (255, 0, 0)

    blabla1 = police_du_texte.render(msg, True, color)

    rectangle_titre = titre.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    rectangle_blabla1 = blabla1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 130))

    screen.blit(titre, rectangle_titre)
    screen.blit(blabla1, rectangle_blabla1)

    pos_souris = pygame.mouse.get_pos()

    # gestion de la souris

    for b in boutons :
        if b["rect"].collidepoint(pos_souris):
            color = (180, 180, 180)
            pygame.draw.rect(screen, (255, 255, 255), b["rect"].inflate(4,4), border_radius = 10, width = 2)
        else :
            color = (100, 100, 100)

        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)


def credits(screen, boutons):

    # quelques variables utiles

    ecart = 80
    hauteur_premier = SCREEN_HEIGHT // 2 - ecart * 2
    
    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(255)     # 0 transparant -> 255 opaque
    floutage.fill((0,0,0))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    police_du_titre = pygame.font.Font("assets/fonts/Pix32.ttf", 50)
    police_du_nom_des_createurs = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 16)

    # le texte du menu pause

    titre = police_du_titre.render("Credits", True, (255, 255, 255))
    les_createurs = police_du_nom_des_createurs.render("Les créateurs de ce superbe jeu vidéo sont :", True, (255, 255, 255))
    karl = police_du_nom_des_createurs.render("Karl Collet", True, (255, 255, 255))
    mathis = police_du_nom_des_createurs.render("Mathis Le Mineur", True, (255, 255, 255))
    theophile = police_du_nom_des_createurs.render("Théophile Grenier", True, (255, 255, 255))

    # pour center ce qu'on a ecrit

    rectangle_du_titre = titre.get_rect(center=(SCREEN_WIDTH // 2, hauteur_premier))
    rectangle_du_nom_des_createurs = les_createurs.get_rect(center=(SCREEN_WIDTH // 2, hauteur_premier + ecart * 1 + 20))
    rectangle_karl = karl.get_rect(center=(SCREEN_WIDTH // 2, hauteur_premier + ecart * 2 + 20))
    rectangle_mathis = mathis.get_rect(center=(SCREEN_WIDTH // 2, hauteur_premier + ecart * 3 + 20))
    rectangle_theophile = theophile.get_rect(center=(SCREEN_WIDTH // 2, hauteur_premier + ecart * 4 + 20))

    # afficher le titre

    screen.blit(titre, rectangle_du_titre)
    screen.blit(les_createurs, rectangle_du_nom_des_createurs)
    screen.blit(karl, rectangle_karl)
    screen.blit(mathis, rectangle_mathis)
    screen.blit(theophile, rectangle_theophile)

    # gestion de la souris

    pos_souris = pygame.mouse.get_pos()

    for b in boutons :
        if b["rect"].collidepoint(pos_souris):
            color = (180, 180, 180)
            pygame.draw.rect(screen, (255, 255, 255), b["rect"].inflate(4,4), border_radius = 10, width = 2)
        else :
            color = (100, 100, 100)

        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)


def crea_boutons_parametrage(dicocle):
    
    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    largeur_du_bouton, hauteur_du_bouton = 400, 50 # Un peu plus large pour le texte
    center_x = SCREEN_WIDTH // 2 - largeur_du_bouton // 2

    hauteur_premier = SCREEN_HEIGHT // 2 - 80
    ecart = 80

    boutons = []
    
    # liste des actions qui peuvent etre modifiees par le joueur

    actions = [
        ("up", "HAUT"), 
        ("down", "BAS"), 
        ("left", "GAUCHE"), 
        ("right", "DROITE")
    ]
    
    # on parcours en recuperant i et le tuble (action, cle)
    for i, (action, text) in enumerate(actions):

        # pygame.key.name() permet de transformer l'identifant de la touche en texte
        key_name = pygame.key.name(dicocle[action]).upper()
        
        display_text = f"{text} : {key_name}"
        
        boutons.append({
            "text": display_text,
            "rect": pygame.Rect(center_x, hauteur_premier + ecart * i, largeur_du_bouton, hauteur_du_bouton),
            "action": f"bind_{action}", # L'action commence par "bind_" pour la repérer facilement
            "surf": font_bouton.render(display_text, True, (255, 255, 255))
        })

    # Bouton de retour à la fin
    boutons.append({
        "text": "RETOUR",
        "rect": pygame.Rect(center_x, hauteur_premier + ecart * 4 + 20, largeur_du_bouton, hauteur_du_bouton),
        "action": "qparam",
        "surf": font_bouton.render("RETOUR", True, (255, 255, 255))
    })

    return boutons


def crea_boutons_home():

    #couleur, taille et position

    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    largeur_du_bouton, hauteur_du_bouton = 300, 60
    center_x = SCREEN_WIDTH // 2 - largeur_du_bouton // 2

    #hauteur d'affichage du premir bouton

    hauteur_premier = SCREEN_HEIGHT // 2 - 50

    #ecart entre les boutons

    ecart = 80

    boutons = [

        #bouton recommencer (la partie repart a 0)

        {
            "text": "COMMENCER",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*1, largeur_du_bouton, hauteur_du_bouton),
            "action": "start",
            "surf": font_bouton.render("COMMENCER", True, (255, 255, 255))
        },

        {
            "text": "PARAMETRES",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*2, largeur_du_bouton, hauteur_du_bouton),
            "action": "parametres",
            "surf": font_bouton.render("PARAMETRES", True, (255, 255, 255))
        },

        {
            "text": "CREDITS",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*3, largeur_du_bouton, hauteur_du_bouton),
            "action": "credits",
            "surf": font_bouton.render("CREDITS", True, (255, 255, 255))
        },

        #bouton quitter (fermer la fenetre)

        {
            "text": "QUITTER",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*4 , largeur_du_bouton, hauteur_du_bouton),
            "action": "quit",
            "surf": font_bouton.render("QUITTER", True, (255, 255, 255))
        }
    ]
    return boutons


def crea_boutons_pause():

    #couleur, taille et position

    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    largeur_du_bouton, hauteur_du_bouton = 300, 60
    center_x = SCREEN_WIDTH // 2 - largeur_du_bouton // 2

    #hauteur d'affichage du premir bouton

    hauteur_premier = SCREEN_HEIGHT // 2 - 50

    #ecart entre les boutons

    ecart = 80

    boutons = [

        #bouton reprendre (fin de pause)

        {
            "text": "REPRENDRE",
            "rect": pygame.Rect(center_x, hauteur_premier, largeur_du_bouton, hauteur_du_bouton),
            "action": "resume",
            "surf": font_bouton.render("REPRENDRE", True, (255, 255, 255))
        },

        #bouton recommencer (la partie repart a 0)

        {
            "text": "RECOMMENCER",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*1, largeur_du_bouton, hauteur_du_bouton),
            "action": "restart",
            "surf": font_bouton.render("RECOMMENCER", True, (255, 255, 255))
        },

        #bouton menu principal (fin de la partie et menu principal)

        {
            "text": "MENU PRINCIPAL",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*2, largeur_du_bouton, hauteur_du_bouton),
            "action": "home",
            "surf": font_bouton.render("MENU PRINCIPAL", True, (255, 255, 255))
        },

        #bouton parametre (affichage des parametres)

        {
            "text": "PARAMETRES",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*3, largeur_du_bouton, hauteur_du_bouton),
            "action": "parametres",
            "surf": font_bouton.render("PARAMETRES", True, (255, 255, 255))
        },

        #bouton quitter (fermer la fenetre)

        {
            "text": "QUITTER LE JEU",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*4 , largeur_du_bouton, hauteur_du_bouton),
            "action": "quit",
            "surf": font_bouton.render("QUITTER LE JEU", True, (255, 255, 255))
        }
    ]
    return boutons


def crea_boutons_gameover():

    #couleur, taille et position

    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    largeur_du_bouton, hauteur_du_bouton = 300, 60
    center_x = SCREEN_WIDTH // 2 - largeur_du_bouton // 2

    #hauteur d'affichage du premir bouton

    hauteur_premier = SCREEN_HEIGHT // 2 - 50

    #ecart entre les boutons

    ecart = 80

    boutons = [

        #bouton recommencer (la partie repart a 0)

        {
            "text": "RECOMMENCER",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*1, largeur_du_bouton, hauteur_du_bouton),
            "action": "restart",
            "surf": font_bouton.render("RECOMMENCER", True, (255, 255, 255))
        },

        #bouton menu principal (fin de la partie et menu principal)

        {
            "text": "MENU PRINCIPAL",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*2, largeur_du_bouton, hauteur_du_bouton),
            "action": "home",
            "surf": font_bouton.render("MENU PRINCIPAL", True, (255, 255, 255))
        },

        #bouton parametre (affichage des parametres)

        {
            "text": "PARAMETRES",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*3, largeur_du_bouton, hauteur_du_bouton),
            "action": "parametres",
            "surf": font_bouton.render("PARAMETRES", True, (255, 255, 255))
        },

        #bouton quitter (fermer la fenetre)

        {
            "text": "QUITTER",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart*4 , largeur_du_bouton, hauteur_du_bouton),
            "action": "quit",
            "surf": font_bouton.render("QUITTER", True, (255, 255, 255))
        }
    ]
    return boutons


def crea_boutons_credits():

    #couleur, taille et position

    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    largeur_du_bouton, hauteur_du_bouton = 300, 60
    center_x = SCREEN_WIDTH // 2 - largeur_du_bouton // 2

    #hauteur d'affichage du premir bouton

    hauteur_premier = SCREEN_HEIGHT // 2 - 50

    #ecart entre les boutons

    ecart = 80

    boutons = [

        #bouton quitter (fermer la fenetre)

        {
            "text": "RETOUR",
            "rect": pygame.Rect(center_x, hauteur_premier + ecart * 5 , largeur_du_bouton, hauteur_du_bouton),
            "action": "qcredits",
            "surf": font_bouton.render("RETOUR", True, (255, 255, 255))
        }
    ]
    return boutons


def crea_boutons_parametroge():

    #couleur, taille et position

    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    largeur_du_bouton, hauteur_du_bouton = 300, 60
    center_x = SCREEN_WIDTH // 2 - largeur_du_bouton // 2

    #hauteur d'affichage du premir bouton

    hauteur_premier = SCREEN_HEIGHT // 2 - 50

    #ecart entre les boutons

    ecart = 80

    boutons = [

        {
            "text": "REPRENDRE",
            "rect": pygame.Rect(center_x, hauteur_premier, largeur_du_bouton, hauteur_du_bouton),
            "action": "qparam",
            "surf": font_bouton.render("REPRENDRE", True, (255, 255, 255))
        }

    ]
    return boutons


def ca_clique(event, boutons):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for b in boutons:
            if b["rect"].collidepoint(event.pos):
                return b["action"]
    return None

