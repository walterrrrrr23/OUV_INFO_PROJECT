
import pygame
from settings import PLAYER_SPEED, ZOOM, PLAYER_ACCELERATION
from utils import load_spritesheet  

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, camera):
        super().__init__()

        self.camera = camera
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
        self.direction = pygame.Vector2(0,0)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
        self.timer = 0
        self.facing_left = False  

        #VAR

        self.speed = PLAYER_SPEED
        self.acceleration = PLAYER_ACCELERATION
        self.max_health = 20
        self.health = 20
        

    def update(self, dt):
        keys = pygame.key.get_pressed()


        dir = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_q],
            keys[pygame.K_s] - keys[pygame.K_z]
        )

        dirmax = 1

        if dir.x != 0 and dir.y != 0:
            dirmax = .75
        self.direction *= 1-PLAYER_ACCELERATION
        if keys[pygame.K_d] :
            self.direction.x += PLAYER_ACCELERATION
            self.direction.x = min(self.direction.x, dirmax)
        elif keys[pygame.K_q] :
            self.direction.x -= PLAYER_ACCELERATION
            self.direction.x = max(self.direction.x, -dirmax)
        if keys[pygame.K_s] :
            self.direction.y += PLAYER_ACCELERATION
            self.direction.y = min(self.direction.y, dirmax)
        elif keys[pygame.K_z] :
            self.direction.y -= PLAYER_ACCELERATION
            self.direction.y = max(self.direction.y, -dirmax)
  
   
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x += self.camera.offset.x

        player_screen_x = self.rect.centerx  

        if mouse_x < player_screen_x:
            self.facing_left = True
        else:
            self.facing_left = False
        if self.direction.length() > .2:
    
            self.current_anim = "walk"
          
            
        else:
            self.current_anim = "idle"

        
        self.vel = self.direction * self.speed*dt
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
        #pygame.draw.rect(window, (255, 0, 0), self.rect, 2) TEST HITBOX JOUEUR
        window.blit(self.image, self.camera.apply(self.rect))
