from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY

import pygame
from settings import ZOOM
from utils import load_spritesheet  

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, camera, player):
        super().__init__()

        self.camera = camera
        self.player = player
        self.frames = load_spritesheet("assets/sprites/coin_sheet.png", 64, 64)

       
        self.animations = {
            "idle": self.frames[0],
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
      
        self.rect = pygame.Rect((0,0), (35,60))
        self.pos = pygame.Vector2(pos)
        self.speed = .1
        self.timer = 0
        self.pickup_radius = 150

    def is_out_of_screen(self, player_pos):
        distance = pygame.math.Vector2.distance_to(self.pos, player_pos)
        if distance > SCREEN_WIDTH:
            return True
        return False 
        
   
    def update(self, dt):
        if self.is_out_of_screen(self.player.pos):
            self.kill()

        playerpos = self.player.pos - self.camera.offset
        selfpos = self.pos - self.camera.offset
        dir = pygame.Vector2(playerpos - selfpos)
        print(dir)
        if dir == pygame.Vector2(0,0):
              self.player.coin += 10
              self.kill()
        if dir.magnitude() < self.pickup_radius :
            if dir.magnitude() < 10 :
                self.player.coin += 10
                self.kill()
            self.pos += dir.normalize() * self.speed
            self.speed += .7
        else:
            self.speed = .1 
        self.rect.center = self.pos
       
        self.timer += dt
        if self.timer >= 1 / self.animation_speed:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_anim])
            self.image = self.animations[self.current_anim][self.frame_index]

        
    def draw(self, window):
       
        screen_rect = self.camera.apply(self.rect)      
        image_rect = self.image.get_rect()    
        image_rect.center = screen_rect.center 
        window.blit(self.image, image_rect)
       
