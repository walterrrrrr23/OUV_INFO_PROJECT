# game.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY
from player import Player
from camera import Camera
from map import load_tiles, draw_checker_map
from weapon import Weapon
from projectile import Projectile
from enemy import Enemy
from menu_pause import HealthBar
class Game:
    def __init__(self):
        self.camera = Camera()
        self.player = Player((0, 0), self.camera)
        self.camera.center(self.player)

        self.sprite_player = pygame.sprite.Group()
        self.sprite_mob = pygame.sprite.Group()
        
        self.sprite_player.add(self.player)


      

        #image arme
        sheet = pygame.image.load("assets/sprites/weaponsheet.png").convert_alpha()
        weapon_image = sheet.subsurface(pygame.Rect(1*TAILLE_SPRITE, 0*TAILLE_SPRITE, 64, 64))
        weapon_image = pygame.transform.scale(weapon_image, (64*ZOOM, 64*ZOOM))

        #image balle
        sheet2 = pygame.image.load("assets/sprites/bulletsheet.png").convert_alpha()
        bullet_image = sheet2.subsurface(pygame.Rect(1*TAILLE_SPRITE, 0*TAILLE_SPRITE, 64, 64))
        bullet_image = pygame.transform.scale(bullet_image, (64*ZOOM, 64*ZOOM))

        bullet_image2 = sheet2.subsurface(pygame.Rect(3*TAILLE_SPRITE, 1*TAILLE_SPRITE, 64, 64))
        bullet_image2 = pygame.transform.scale(bullet_image2, (64*ZOOM, 64*ZOOM))

        #def arme (à qui on associe une balle (=son image))
        self.weapon = Weapon(self.player, weapon_image, self.camera, bullet_image)
        #self.sprite_player.add(self.weapon) update weapon individuellement

        self.enemy = Enemy((100, 100), self.camera, self.player, bullet_image2)
        self.sprite_mob.add(self.enemy)

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

        if self.player.pos.x - self.camera.offset.x > SCREEN_WIDTH - SCREEN_WIDTH/CAMERA_OFFSET_THRESHOLD :
            self.camera.update(pygame.Vector2(self.player.vel.x + self.player.knockdirection.x, 0))
        if self.player.pos.y - self.camera.offset.y > SCREEN_HEIGHT  - SCREEN_HEIGHT/CAMERA_OFFSET_THRESHOLD  :
            self.camera.update(pygame.Vector2(0,self.player.vel.y +self.player.knockdirection.y ))
        if self.player.pos.x - self.camera.offset.x < SCREEN_WIDTH/CAMERA_OFFSET_THRESHOLD :
           self.camera.update(pygame.Vector2(self.player.vel.x + self.player.knockdirection.x, 0))
        if self.player.pos.y - self.camera.offset.y < SCREEN_HEIGHT/CAMERA_OFFSET_THRESHOLD :
            self.camera.update(pygame.Vector2(0,self.player.vel.y + self.player.knockdirection.y))

    def draw(self, window):
        draw_checker_map(window, self.camera, self.tile1, self.tile2)
        
        for sprite in self.sprite_mob:
            sprite.draw(window)

        for sprite in self.sprite_player:
           sprite.draw(window)

        self.weapon.draw(window)

        #GUI

        HealthBar(self.player, window)
