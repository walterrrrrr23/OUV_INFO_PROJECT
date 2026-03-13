# game.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY
from player import Player
from camera import Camera
from map import load_tiles, draw_checker_map
from weapon import Weapon
from projectile import Projectile
from enemy import Enemy
from coin import Coin
from menu_pause import HealthBar
from damage_indicator import Damage_Indicator
class Game:
    def __init__(self):
        self.camera = Camera()
        self.player = Player((0, 0), self.camera)
        self.camera.center(self.player)

        self.sprite_player = pygame.sprite.Group()
        self.sprite_mob = pygame.sprite.Group()
        self.sprite_coins = pygame.sprite.Group()
<<<<<<< HEAD
        self.sprite_bullets = pygame.sprite.Group()
        self.damage_indicator = pygame.sprite.Group()
        
        self.sprite_player.add(self.player)

      

      


       

        #def arme (à qui on associe un nom)
=======

        #définition du joueur et de son arme 
        self.sprite_player.add(self.player)
>>>>>>> 128f513212106673b685953086ff5333e11b1f05
        self.weapon = Weapon(self.player, self.camera, "Revolver")

        self.enemy = Enemy((100, 100), self.camera, self.player, "Joker", self.sprite_coins, self.sprite_bullets, self.damage_indicator)
        self.sprite_mob.add(self.enemy)

<<<<<<< HEAD
      

        self.tile1, self.tile2 = load_tiles("assets/sprites/tiles.png")

       

    def update(self, dt):
        self.camera.calclateOffset()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = ((mouse_x - SCREEN_WIDTH/2)/SCREEN_WIDTH) * MOUSE_SENSITIVITY
        mouse_y = ((mouse_y - SCREEN_WIDTH/2)/SCREEN_HEIGHT) * MOUSE_SENSITIVITY

        self.camera.updateMouse(pygame.Vector2(mouse_x, mouse_y))

        self.sprite_player.update(dt) #->player.
        self.weapon.update(dt, self.sprite_mob)
        self.sprite_mob.update(dt, self.sprite_player)
        self.sprite_coins.update(dt)
        self.sprite_bullets.update(dt, self.sprite_player)
        self.damage_indicator.update(dt)

=======
        #définition des tiles -> map
        self.tile1, self.tile2 = load_tiles("assets/sprites/tiles.png")

    def update_camera(self):
        self.camera.calculateOffset()
>>>>>>> 128f513212106673b685953086ff5333e11b1f05
        if self.player.pos.x - self.camera.offset.x > SCREEN_WIDTH - SCREEN_WIDTH/CAMERA_OFFSET_THRESHOLD :
            self.camera.update(pygame.Vector2(self.player.vel.x , 0))
        if self.player.pos.y - self.camera.offset.y > SCREEN_HEIGHT  - SCREEN_HEIGHT/CAMERA_OFFSET_THRESHOLD  :
            self.camera.update(pygame.Vector2(0,self.player.vel.y  ))
        if self.player.pos.x - self.camera.offset.x < SCREEN_WIDTH/CAMERA_OFFSET_THRESHOLD :
           self.camera.update(pygame.Vector2(self.player.vel.x , 0))
        if self.player.pos.y - self.camera.offset.y < SCREEN_HEIGHT/CAMERA_OFFSET_THRESHOLD :
            self.camera.update(pygame.Vector2(0,self.player.vel.y ))

    def update_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = ((mouse_x - SCREEN_WIDTH/2)/SCREEN_WIDTH) * MOUSE_SENSITIVITY
        mouse_y = ((mouse_y - SCREEN_WIDTH/2)/SCREEN_HEIGHT) * MOUSE_SENSITIVITY
        self.camera.updateMouse(pygame.Vector2(mouse_x, mouse_y))

    def update(self, dt):
        self.update_mouse()
        self.sprite_player.update(dt) #->player.
        self.weapon.update(dt, self.sprite_mob)
        self.sprite_mob.update(dt, self.sprite_player)
        self.sprite_coins.update(dt)
        self.update_camera()


    def draw(self, window):
        draw_checker_map(window, self.camera, self.tile1, self.tile2)
        for sprite in self.sprite_coins:
            sprite.draw(window)

        for sprite in self.sprite_mob:
            sprite.draw(window)

        for sprite in self.sprite_player:
           sprite.draw(window)

        self.weapon.draw(window)
        
        for sprite in self.sprite_bullets:
       
           sprite.draw(window)

        for sprite in self.damage_indicator:
       
           sprite.draw(window)
        #GUI

        HealthBar(self.player, window)
