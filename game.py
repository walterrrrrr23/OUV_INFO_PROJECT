# game.py
import pygame
from settings import BG_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from camera import Camera

class Game:
    def __init__(self, screen):
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()

        self.player = Player((0, 0))
        self.all_sprites.add(self.player)

        self.camera = Camera()

    def update(self, dt):
        self.all_sprites.update(dt)
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill(BG_COLOR)

        for sprite in self.all_sprites:
            self.screen.blit(
                sprite.image,
                self.camera.apply(sprite.rect)
            )
