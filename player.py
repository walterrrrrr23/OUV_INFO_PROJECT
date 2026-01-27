# player.py
import pygame
from settings import PLAYER_SPEED, PLAYER_SIZE, PLAYER_COLOR

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(PLAYER_COLOR)

        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.speed = PLAYER_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        direction = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_q],
            keys[pygame.K_s] - keys[pygame.K_z]
        )

        if direction.length() > 0:
            direction.normalize_ip()

        self.pos += direction * self.speed * dt
        self.rect.center = self.pos
