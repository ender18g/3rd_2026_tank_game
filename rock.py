import pygame
from pathlib import Path
ASSETS = Path(r"kenney_top-down-tanks-remastered\PNG\Default size")
from random import randint, uniform
from missile import Missile


class Rock(pygame.sprite.Sprite):
    def __init__(self,size,num_rocks,player,missiles, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ASSETS / 'crateMetal.png')
        self.image = pygame.transform.rotozoom(self.image, randint(0,360), uniform(0.8,2.0))
        self.x = randint(0, size[0])
        self.y = randint(0, size[1])
        self.vx = 0 #randint(-5,5)/10
        self.vy = 0 #randint(-5,5)/10
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.exploded = False
        self.t_e = 0
        self.width, self.height = size
        self.num_rocks = num_rocks
        self.player = player
        self.missiles = missiles
        self.shoot_delay = 3_000 # in ms
        self.t_shot = 0
        self.screen = screen
        
    def shoot(self):
        # generate random number
        num = uniform(0,100)
        if num < 0.3:
            new_missile = Missile(self.x, self.y, self.player, self.screen)
            self.missiles.add(new_missile)
        
        
    def explode(self):
        # change the image
        if not self.exploded:
            self.image = pygame.image.load(ASSETS / 'explosionSmoke4.png')
            self.t_e = pygame.time.get_ticks()
            self.exploded = True
            self.num_rocks[0]  = self.num_rocks[0] + 0
    
    def update(self):
        self.x += self.vx
        self.y +=self.vy
        self.rect.center = (self.x,self.y)
        # if exploded and enough time passed
        t_now = pygame.time.get_ticks()
        if self.exploded and t_now - self.t_e > 500:
            self.kill()
        
        # check to see if out of bounds
        if self.x < 0 or self.x>self.width:
            self.vx = -self.vx
        if self.y < 0 or self.y>self.height:
            self.vy = -self.vy
        
        # shoot on every update
        self.shoot()
         
        
        






    