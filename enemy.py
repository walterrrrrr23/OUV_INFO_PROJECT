
import pygame
from settings import PLAYER_SPEED, ZOOM, PLAYER_ACCELERATION
from utils import load_spritesheet  

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, camera, target):
        super().__init__()

        self.camera = camera
        self.target = target
        self.frames = load_spritesheet("assets/sprites/enemies/player_sheet.png", 64, 64)

       
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
        self.direction = pygame.Vector2(0,0)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
 
        self.timer = 0
        self.facing_left = False  



        #VARIABLES

        self.speed = 150
        self.acceleration = .1
        self.damage = 10

    def update(self, dt):
      


        dir = self.target.pos - self.pos

        self.direction = dir.normalize()

        dirmax = 1

     
  
   
     

        if self.pos.x > self.target.pos.x :
            self.facing_left = True
        else:
            self.facing_left = False
        if self.direction.length() > .2:
    
            self.current_anim = "walk"
          
            
        else:
            self.current_anim = "idle"

        
        self.vel = self.direction * self.speed*dt
        print(self.direction)
        self.pos += self.vel
        self.rect.center = self.pos

       
        self.timer += dt
        if self.timer >= 1 / self.animation_speed:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_anim])
            self.image = self.animations[self.current_anim][self.frame_index]

        
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, window):
        window.blit(self.image, self.camera.apply(self.rect))
