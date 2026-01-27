# camera.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self):
        self.offset = pygame.Vector2()
    def center(self, target):
        self.offset.x += target.rect.centerx - SCREEN_WIDTH // 2
        self.offset.y += target.rect.centery - SCREEN_HEIGHT // 2
    def update(self, vect):
        self.offset += vect
     

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)
