import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PAUSE
"""
# 1. Initialisation
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Arial", 50)
clock = pygame.time.Clock()

# États du jeu
en_pause = False
running = True

while running:
    # 2. Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Si on appuie sur P
                en_pause = not en_pause  # On inverse l'état (Toggle)

    # 3. Logique d'affichage
    if en_pause:
        # --- AFFICHAGE DU MENU ---
        screen.fill((50, 50, 50)) # Fond gris foncé
        texte_menu = font.render("PAUSE - Appuyez sur P pour reprendre", True, (255, 255, 255))
        screen.blit(texte_menu, (100, 250))
    else:
        # --- AFFICHAGE DU JEU ---
        screen.fill((0, 128, 255)) # Fond bleu (ton jeu)
        # Ici, mets la logique de mouvement et de dessin de ton jeu

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""
def Pause():

    print("test")
    
    """pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("menu")

    clock = pygame.time.Clock()

    screen_menu = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("Arial", 50)

    running = True

    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
        
        if PAUSE:
            # --- AFFICHAGE DU MENU ---
            screen_menu.fill((50, 50, 50)) # Fond gris foncé
            texte_menu = font.render("PAUSE - Appuyez sur P pour reprendre", True, (255, 255, 255))
            screen_menu.blit(texte_menu, (100, 250))

    pygame.quit()"""