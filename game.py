# game.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_OFFSET_THRESHOLD, ZOOM, TAILLE_SPRITE, MOUSE_SENSITIVITY
from player import Player
from camera import Camera
from map import load_tiles, draw_checker_map
from weapon import Weapon
class Game:
    def __init__(self, screen):
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.camera = Camera()
        self.player = Player((0, 0), self.camera)
        self.all_sprites.add(self.player)

       
        self.camera.center(self.player)

        sheet = pygame.image.load("assets/sprites/weaponsheet.png").convert_alpha()

        weapon_image = sheet.subsurface(pygame.Rect(4*TAILLE_SPRITE, 0*TAILLE_SPRITE, 64, 64))
        weapon_image = pygame.transform.scale(weapon_image, (64*ZOOM, 64*ZOOM))


        self.weapon = Weapon(self.player, weapon_image, self.camera)
        self.all_sprites.add(self.weapon)
        self.tile1, self.tile2 = load_tiles("assets/sprites/tiles.png")

    def update(self, dt):
        self.camera.calclateOffset()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = ((mouse_x - SCREEN_WIDTH/2)/SCREEN_WIDTH) * MOUSE_SENSITIVITY
        mouse_y = ((mouse_y - SCREEN_WIDTH/2)/SCREEN_HEIGHT) * MOUSE_SENSITIVITY

        self.camera.updateMouse(pygame.Vector2(mouse_x, mouse_y))

        self.all_sprites.update(dt)
        if self.player.pos.x - self.camera.offset.x > SCREEN_WIDTH - SCREEN_WIDTH/CAMERA_OFFSET_THRESHOLD :
            self.camera.update(pygame.Vector2(self.player.vel.x, 0))
        if self.player.pos.y - self.camera.offset.y > SCREEN_HEIGHT  - SCREEN_HEIGHT/CAMERA_OFFSET_THRESHOLD  :
            self.camera.update(pygame.Vector2(0,self.player.vel.y))
        if self.player.pos.x - self.camera.offset.x < SCREEN_WIDTH/CAMERA_OFFSET_THRESHOLD :
           self.camera.update(pygame.Vector2(self.player.vel.x, 0))
        if self.player.pos.y - self.camera.offset.y < SCREEN_HEIGHT/CAMERA_OFFSET_THRESHOLD :
            self.camera.update(pygame.Vector2(0,self.player.vel.y))

    def draw(self):
        draw_checker_map(self.screen, self.camera, self.tile1, self.tile2)

        for sprite in self.all_sprites:
            self.screen.blit(
                sprite.image,
                self.camera.apply(sprite.rect)
            )
