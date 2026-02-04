import pygame
import math

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
        self.rect = self.image.get_rect(center=self.pos) #Hitbox de la dimension du sprite

        angle = self.direction.angle_to(pygame.Vector2(1,0))

        self.image = pygame.transform.rotate(self.image, angle)

    def update(self, dt):
        self.pos = self.pos + self.direction*self.speed*dt
        self.rect.center = self.pos

    def draw(self, window):
        window.blit(self.image, self.camera.apply(self.rect))
        #pygame.draw.rect(window, (255, 0, 0), self.rect, 2) TEST HITBOX ARMES
        




    

    

        

