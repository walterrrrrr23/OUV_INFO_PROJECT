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
        self.rect = pygame.Rect((0,0), (10,10))
        self.img_bullet = image_projectile
        self.last = 0
        self.sprite_projectiles = pygame.sprite.Group()


        #VAR

        self.screenshakeammount = 8
        self.screenshaketime = 5
        self.damage = 3
        self.kb = 10
        self.bulletspeed = 1500
        self.cooldown = 300 #en ticks
        self.recoil_angle = 0
        self.recoil_kick = 40 #angle        
        self.recoil_return_speed = 100 #vitesse
        

    def display_weapon(self, dt):
        """
        Rotation de l'arme dans la direction de la souris
        """
        self.rect.center = self.player.pos #position du joueur
        mouse_x, mouse_y = pygame.mouse.get_pos() #postion de la souris
        mouse_x += self.camera.offset.x #déplacement en x de la souris relativement à la caméra
        mouse_y += self.camera.offset.y #déplacement en y de la souris relativement à la caméra
        dx = mouse_x - self.player.pos.x #distance en x entre la souris et le joueur
        dy = mouse_y - self.player.pos.y #distance en x entre la souris et le joueur
        angle = math.degrees(math.atan2(-dy, dx)) #angle entre l'arme et le joueur 
        
        if self.player.facing_left :
             angle -= self.recoil_angle #applique le recoil
        else:
             angle += self.recoil_angle #applique le recoil

       
        handoffset =  pygame.Vector2(0,10)
        if self.player.facing_left:
            handoffset.x = -3
            self.image = pygame.transform.flip(self.original_image, False, True) #direction de l'arme
            self.image = pygame.transform.rotate(self.image, angle) #angle de l'arme --> direction de la souris
        else:
            handoffset.x = 3
            self.image = pygame.transform.rotate(self.original_image, angle)

        self.rect = self.image.get_rect(center=self.player.pos + handoffset) #modification de l'affichage


        #retourne l'arme a son orientation normale de maniere smooth
        self.recoil_angle -= self.recoil_return_speed * dt
        if self.recoil_angle < 0:
            self.recoil_angle = 0
    def shoot(self):
        #direction de la balle relativement à la postion du joueur et de la caméra (cf. display_weapon)
        self.last = pygame.time.get_ticks()
        
        
        bullet_pos = pygame.math.Vector2.copy(self.player.pos)
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        mouse_pos += self.camera.offset
        direction = (mouse_pos - bullet_pos).normalize()
        bullet_pos += direction*64
        
        #Création du projectile
        self.player_shoot = Projectile(self.camera, self.img_bullet, bullet_pos, direction, self.bulletspeed, self.damage, self.kb)
        self.sprite_projectiles.add(self.player_shoot)

        #creation d'un recoil = petit angle de différence quand on tire pour plus de réalisme
        self.recoil_angle = 0
       
        self.recoil_angle += self.recoil_kick

    def draw(self, window):
        screen_rect = self.camera.apply(self.rect)      
        image_rect = self.image.get_rect()    
        image_rect.center = screen_rect.center 
        window.blit(self.image, image_rect)
        #pygame.draw.rect(window, (255, 0, 0), screen_rect, 2)
        for sprite in self.sprite_projectiles:
            sprite.draw(window)

    def update(self, dt, enemies):
        self.display_weapon(dt)
        mouse_clicks = pygame.mouse.get_pressed()[0]#num_buttons=1)
        now = pygame.time.get_ticks()
        if mouse_clicks and now - self.last > self.cooldown :
            self.camera.screenshake(self.screenshaketime, self.screenshakeammount)
            self.shoot()
        for projectile in self.sprite_projectiles:
            projectile.update(dt, enemies)
            if projectile.is_out_of_screen(self.player.pos):
                projectile.kill()
        
