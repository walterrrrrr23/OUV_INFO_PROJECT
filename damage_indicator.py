from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY

import pygame
from settings import ZOOM
from utils import load_spritesheet  
import random
class Damage_Indicator(pygame.sprite.Sprite):
    def __init__(self, pos, camera, text):
        super().__init__()
        self.font_text = pygame.font.Font("assets/fonts/Pix32.ttf", 15)
        self.info1_surface = self.font_text.render(f"{text}", True, (255, 255, 255))
        self.pos = pos
        self.camera = camera
        self.info_rect = self.info1_surface.get_rect(center=(pos))
        self.timer = 0
        self.max_time = .3
      
    def update(self, dt):

      
      
               
    
      
        self.info_rect.center = self.pos
        self.pos += pygame.Vector2(0, (-30*dt)/(self.timer + .1))
        self.info_rect = self.info1_surface.get_rect(center=(self.pos))
        self.timer += dt
        if self.timer >=  self.max_time :
            self.kill()
         

        
    def draw(self, window):
       
        screen_rect = self.camera.apply(self.info_rect)      
        
        window.blit(self.info1_surface, screen_rect)
       




