import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE

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

    font_title = pygame.font.SysFont("arial", 80, bold=True)
    font_text = pygame.font.SysFont("arial", 40)
    info1_surface = font_text.render(f"{health} / {maxhealth}", True, (200, 200, 200))

    info_rect = info1_surface.get_rect(center=(sizex//2 + offsetx, sizey//2 + offsety))

    display.blit(info1_surface, info_rect)
    
def pause(screen):

    #mettre en pause game
    #faire apparaitre la sourie
    #faire des boutons

    # floutage

    floutage = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    floutage.set_alpha(150)     # 0 transparant -> 255 opaque
    floutage.fill((0,0,0))
    screen.blit(floutage,(0,0))

    # les polices d'ecritures du menu pause

    font_title = pygame.font.SysFont("arial", 80, bold=True)
    font_text = pygame.font.SysFont("arial", 40)

    # le texte du menu pause

    title_surface = font_title.render("PAUSE", True, (255, 255, 255))
    info1_surface = font_text.render("Appuyez sur P pour reprendre", True, (200, 200, 200))
    info2_surface = font_text.render("Appuyez sur ESC pour quitter", True, (200, 200, 200))

    # pour center ce qu'on a ecrit

    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    info_rect = info1_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
    quit_rect = info2_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))

    # bouton pour repprendre

    # afficher le titre

    screen.blit(title_surface, title_rect)

    # afficher le texte

    screen.blit(info1_surface, info_rect)
    screen.blit(info2_surface, quit_rect)