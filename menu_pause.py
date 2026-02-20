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

    font_title = pygame.font.Font("assets/fonts/Pix32.ttf", 40)
    font_text = pygame.font.Font("assets/fonts/Pix32.ttf", 20)
    info1_surface = font_text.render(f"{health} / {maxhealth}", True, (200, 200, 200))

    info_rect = info1_surface.get_rect(center=(bar_lenght_pixel//2 + offsetx, sizey//2 + offsety))

    display.blit(info1_surface, info_rect)

    sheet = pygame.image.load("assets/sprites/coin_sheet.png").convert_alpha()
    coin = sheet.subsurface(pygame.Rect(0*TAILLE_SPRITE, 0*TAILLE_SPRITE, 64, 64))
    coin = pygame.transform.scale(coin, (64*ZOOM*1.5, 64*ZOOM*1.5))

    rect = pygame.Rect((0,0), (10,10))
    rect.center = (offsetx-90, offsety + 15)
    display.blit(coin, rect)

    info1_surface = font_text.render(f"{player.coin}", True, (200, 200, 200))

    info_rect = info1_surface.get_rect(center=(offsetx+60, offsety+120))

    display.blit(info1_surface, info_rect)
    
def pause(screen, boutons):

    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(150)     # 0 transparant -> 255 opaque
    floutage.fill((0,0,0))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    font_title = pygame.font.Font("assets/fonts/Pix32.ttf", 50)
    #font_text = pygame.font.SysFont("arial", 40)

    # le texte du menu pause

    title_surface = font_title.render("PAUSE", True, (255, 255, 255))
    #info1_surface = font_text.render("Appuyez sur P pour reprendre", True, (200, 200, 200))
    #info2_surface = font_text.render("Appuyez sur ESC pour quitter", True, (200, 200, 200))

    # pour center ce qu'on a ecrit

    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    #info_rect = info1_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
    #quit_rect = info2_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))

    # afficher le titre

    screen.blit(title_surface, title_rect)

    # afficher le texte

    #screen.blit(info1_surface, info_rect)
    #screen.blit(info2_surface, quit_rect)

    # afficher les boutons

    pos_souris = pygame.mouse.get_pos()

    for b in boutons :
        # Couleur change si survolé
        color = (150, 150, 150) if b["rect"].collidepoint(pos_souris) else (100, 100, 100)
        pygame.draw.rect(screen, color, b["rect"], border_radius=10)
        
        text_rect = b["surf"].get_rect(center=b["rect"].center)
        screen.blit(b["surf"], text_rect)


def crea_boutons():

    #couleur, taille et position

    font_bouton = pygame.font.Font("assets/fonts/Pix32Thin.ttf", 20)
    bouton_width, bouton_height = 300, 60
    center_x = SCREEN_WIDTH // 2 - bouton_width // 2

    #boutons : repprendre et quitter

    boutons = [
        {
            "text": "REPRENDRE",
            "rect": pygame.Rect(center_x, SCREEN_HEIGHT // 2, bouton_width, bouton_height),
            "action": "resume",
            "surf": font_bouton.render("REPRENDRE", True, (255, 255, 255))
        },
        {
            "text": "QUITTER",
            "rect": pygame.Rect(center_x, SCREEN_HEIGHT // 2 + 80, bouton_width, bouton_height),
            "action": "quit",
            "surf": font_bouton.render("QUITTER", True, (255, 255, 255))
        }
    ]
    return boutons

def ca_clique(event, boutons):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for b in boutons:
            if b["rect"].collidepoint(event.pos):
                return b["action"]
    return None