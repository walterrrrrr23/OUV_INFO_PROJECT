import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, camera, image, x, y, speed, damage, knockback=0): #Knockback optionnel (0 par défault)
        super().__init__()
        self.cam = camera
        self.image = image
        self.pos = pygame.Vector2(x,y)
        self.speed = speed #Vecteur vitesse constante (en direction du player)
        self.damage = damage
        self.kb = knockback
        self.rect = self.image.get_rect(center=self.pos) #Hitbox de la dimension du sprite

    def update(self, dt):
        self.pos = self.pos + self.speed*dt
        self.rect.center = self.pos
        




    

    

        

