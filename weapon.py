# weapon.pyimport pygame
import math
import pygame
from projectile import Projectile

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, image_surface, camera, image_projectile):
        super().__init__()
        self.camera = camera
        self.player = player 
        self.original_image = image_surface
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.player.pos)
        self.img_bullet = image_projectile

        self.sprite_projectiles = pygame.sprite.Group()

    def display_weapon(self):
        """
        Rotation de l'arme dans la direction de la souris
        """
        self.rect.center = self.player.pos #position du jouer
        mouse_x, mouse_y = pygame.mouse.get_pos() #postion de la souris
        mouse_x += self.camera.offset.x #déplacement en x de la souris relativement à la caméra
        mouse_y += self.camera.offset.y #déplacement en y de la souris relativement à la caméra
        dx = mouse_x - self.player.pos.x #distance en x entre la souris et le joueur
        dy = mouse_y - self.player.pos.y #distance en x entre la souris et le joueur
        angle = math.degrees(math.atan2(-dy, dx)) #angle entre l'arme et le joueur 
        
        handoffset =  pygame.Vector2(0,10)
        if self.player.facing_left:
            handoffset.x = -3
            self.image = pygame.transform.flip(self.original_image, False, True) #direction de l'arme
            self.image = pygame.transform.rotate(self.image, angle) #angle de l'arme --> direction de la souris
        else:
            handoffset.x = 3
            self.image = pygame.transform.rotate(self.original_image, angle)

        self.rect = self.image.get_rect(center=self.player.pos + handoffset) #modification de l'affichage

    def shoot(self):
        #direction de la balle relativement à la postion du joueur et de la caméra (cf. display_weapon)
        x, y = self.rect.right, self.rect.centery
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x += self.camera.offset.x
        mouse_y += self.camera.offset.y
        dx = mouse_x - self.player.pos.x
        dy = mouse_y - self.player.pos.y

        #Création du projectile
        self.player_shoot = Projectile(self.camera, self.img_bullet, x, y, pygame.Vector2(dx, dy).normalize(), 500, 0, 0)
        self.sprite_projectiles.add(self.player_shoot)

    def draw(self, window):
        window.blit(self.image, self.camera.apply(self.rect))
        for sprite in self.sprite_projectiles:
            sprite.draw(window)

    def update(self, dt):
        self.display_weapon()
        mouse_clicks = pygame.mouse.get_pressed()[0]#num_buttons=1)
        if mouse_clicks:
            self.shoot()
        self.sprite_projectiles.update(dt)
        
