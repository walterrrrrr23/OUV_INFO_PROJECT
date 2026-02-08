import pygame
import math
from settings import SCREEN_WIDTH

class Projectile(pygame.sprite.Sprite):
    def __init__(self, camera, image, position, direction, speed, damage, knockback=0): #Knockback optionnel (0 par défault)
        super().__init__()
        self.camera = camera
        self.image = image
        self.pos = position
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.kb = knockback
        self.rect = pygame.Rect(position, (15,15))

        angle = self.direction.angle_to(pygame.Vector2(1,0))

        self.image = pygame.transform.rotate(self.image, angle)

    def is_out_of_screen(self, player_pos):
        distance = pygame.math.Vector2.distance_to(self.pos, player_pos)
        if distance > SCREEN_WIDTH:
            return True
        return False

    def update(self, dt, targetlist):
        self.pos = self.pos + self.direction*self.speed*dt
        self.rect.center = self.pos

        hit_list = pygame.sprite.spritecollide(self, targetlist, False)

        for enemy in hit_list:
            enemy.take_damage(self.damage, self.direction, self.kb)
            self.kill()  
            break

    def draw(self, window):
        screen_rect = self.camera.apply(self.rect)      
        image_rect = self.image.get_rect()    
        image_rect.center = screen_rect.center 
        window.blit(self.image, image_rect)
        #pygame.draw.rect(window, (255, 0, 0), screen_rect, 2)
        




    

    

        

