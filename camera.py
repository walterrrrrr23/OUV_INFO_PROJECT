# camera.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self):
        self.offset = pygame.Vector2()
        self.mouseoffset = pygame.Vector2()
        self.worldoffset = pygame.Vector2()
    def center(self, target):
        self.worldoffset.x += target.rect.centerx - SCREEN_WIDTH // 2
        self.worldoffset.y += target.rect.centery - SCREEN_HEIGHT // 2
    def update(self, vect):
        self.worldoffset += vect 
    def updateMouse(self, vect):
        self.mouseoffset = vect
    def calclateOffset(self):
        self.offset = self.mouseoffset + self.worldoffset

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)
