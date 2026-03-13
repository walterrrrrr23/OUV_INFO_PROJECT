from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY

import pygame
from settings import ZOOM
from utils import load_spritesheet  
import random
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, camera, player, coin_id):
        super().__init__()
        self.value = 0
        self.coin_id = coin_id
        self.camera = camera
        self.player = player
        self.frames = load_spritesheet("assets/sprites/coin_sheet.png", 64, 64)
        self.animations = 0
        print(len(self.frames)) 
        if self.coin_id == "copper_coin" :
            self.animations = {
            "idle": self.frames[2],
            }
            self.value = 1
        elif self.coin_id == "iron_coin" :
            self.animations = {
            "idle": self.frames[1],
            }
            self.value = 5
        elif self.coin_id == "gold_coin" :
            self.animations = {
            "idle": self.frames[0],
            }
            self.value = 10
       

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
        self.target = pygame.Vector2(pos + pygame.Vector2(random.randint(-70,70),random.randint(-30,30)))
        self.speed = .1
        self.timer = 0
        self.pickup_radius = 150

        self.start = pos.copy()

        self.duration = .5      
        self.time_passed = 0.0
        self.arc_height = 65    
        self.done = False

    def is_out_of_screen(self, player_pos):
        distance = pygame.math.Vector2.distance_to(self.pos, player_pos)
        if distance > SCREEN_WIDTH:
            return True
        return False 
        
   
    def update(self, dt):

        if not self.done:
      

            self.time_passed += dt
            t = min(self.time_passed / self.duration, 1)

            
            base = self.start.lerp(self.target, t)

           
            height = 4 * self.arc_height * t * (1 - t)

            self.pos.x = base.x
            self.pos.y = base.y - height

            if t >= 1:
                self.pos = self.target
                self.done = True
        if self.is_out_of_screen(self.player.pos):
            self.kill()

        playerpos = self.player.pos - self.camera.offset
        selfpos = self.pos - self.camera.offset
        dir = pygame.Vector2(playerpos - selfpos)
       
        if dir == pygame.Vector2(0,0):
              self.player.coin += self.value
              self.kill()
        if dir.magnitude() < self.pickup_radius :
            if dir.magnitude() < 10 :
                self.player.coin += self.value
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
       
