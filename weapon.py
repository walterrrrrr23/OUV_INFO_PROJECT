# weapon.pyimport pygame
import math
import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, image_surface, camera):
        super().__init__()
        self.camera = camera
        self.player = player 
        self.original_image = image_surface
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.player.pos)

    def update(self, dt):
        
        self.rect.center = self.player.pos

   
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x += self.camera.offset.x
        mouse_y += self.camera.offset.y

     
        dx = mouse_x - self.player.pos.x
        dy = mouse_y - self.player.pos.y
        angle = math.degrees(math.atan2(-dy, dx))  

        handoffset =  pygame.Vector2(0,10)
        if self.player.facing_left:
            handoffset.x = -3
            self.image = pygame.transform.flip(self.original_image, False, True)
           
            self.image = pygame.transform.rotate(self.image, angle)
        else:
            handoffset.x = 3
            self.image = pygame.transform.rotate(self.original_image, angle)

     
        self.rect = self.image.get_rect(center=self.player.pos + handoffset)
