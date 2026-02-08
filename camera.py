# camera.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Camera:
    def __init__(self):
        self.offset = pygame.Vector2()
        self.mouseoffset = pygame.Vector2()
        self.worldoffset = pygame.Vector2()

        self.shake_time = 0
        self.shake_intensity = 0
        self.shake_offset = pygame.Vector2()

    def screenshake(self, time_ticks, intensity):
        self.shake_time = time_ticks
        self.shake_intensity = intensity

   
    def update_shake(self):
        if self.shake_time > 0:
            self.shake_time -= 1

          
            self.shake_offset.x = random.randint(-self.shake_intensity, self.shake_intensity)
            self.shake_offset.y = random.randint(-self.shake_intensity, self.shake_intensity)

        else:
            self.shake_offset.update(0, 0)


    def center(self, target):
        self.worldoffset.x += target.rect.centerx - SCREEN_WIDTH // 2
        self.worldoffset.y += target.rect.centery - SCREEN_HEIGHT // 2
    def update(self, vect):
        self.worldoffset += vect 
    def updateMouse(self, vect):
        self.mouseoffset = vect
    def calclateOffset(self):
        self.update_shake()
        self.offset = self.mouseoffset + self.worldoffset + self.shake_offset

    

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)
