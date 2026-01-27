
import pygame
from settings import PLAYER_SPEED, ZOOM
from utils import load_spritesheet  

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

      
        self.frames = load_spritesheet("assets/sprites/player_sheet.png", 64, 64)

       
        self.animations = {
            "idle": self.frames[0],
            "walk": self.frames[1]
        }

        for state, frames in self.animations.items():
            for i in range(len(frames)):
                frames[i] = pygame.transform.scale(
                frames[i],
                (frames[i].get_width()*ZOOM, frames[i].get_height()*ZOOM)
        )
        self.current_anim = "idle"
        self.frame_index = 0
        self.animation_speed = 10 
        self.image = self.animations[self.current_anim][self.frame_index]

        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.timer = 0
        self.facing_left = False  

    def update(self, dt):
        keys = pygame.key.get_pressed()


        direction = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_q],  
            keys[pygame.K_s] - keys[pygame.K_z]  
        )

        if direction.length() > 0:
            direction.normalize_ip()
            self.current_anim = "walk"
          
            if direction.x < 0:
                self.facing_left = True
            elif direction.x > 0:
                self.facing_left = False
        else:
            self.current_anim = "idle"

      
        self.vel = direction * self.speed * dt
        self.pos += self.vel
        self.rect.center = self.pos

       
        self.timer += dt
        if self.timer >= 1 / self.animation_speed:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_anim])
            self.image = self.animations[self.current_anim][self.frame_index]

        
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)
