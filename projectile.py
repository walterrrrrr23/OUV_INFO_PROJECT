import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, camera, image, x, y, direction, speed, damage, knockback=0): #Knockback optionnel (0 par défault)
        super().__init__()
        self.camera = camera
        self.image = image
        self.pos = pygame.Vector2(x,y)
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.kb = knockback
        self.rect = self.image.get_rect(center=self.pos) #Hitbox de la dimension du sprite

    def update(self, dt):
        self.pos = self.pos + self.direction*self.speed*dt
        self.rect.center = self.pos

    def draw(self, window):
        window.blit(self.image, self.camera.apply(self.rect))
        




    

    

        

