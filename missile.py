import pygame
from math import atan2, sin, cos, pi
from pathlib import Path
from random import randint
ASSETS = Path(r"kenney_top-down-tanks-remastered\PNG\Default size")

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, player, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 1
        self.theta = 0 # degrees
        self.player = player
        self.image0 = pygame.image.load(ASSETS / 'bulletRed3_outline.png')
        self.image0 =  pygame.transform.rotate(self.image0, -90)
        self.image = self.image0
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.kill_delay = 500
        self.explode_time = 0
        self.exploded = False
        self.offset_x = randint(-100, 100)
        self.offset_y = randint(-100, 100)
        self.set_init()
        self.screen = screen
        self.screen_rect = screen.get_rect()
    
    def set_init(self):
        # update theta (simple lag pursuit)
        delta_x = self.player.x -self.x
        delta_y = self.player.y - self.y
        
        # update theta (lead pursuit)
        lead_gain = 0
        delta_x = self.player.x + self.offset_x + self.player.vx * lead_gain - self.x
        delta_y = self.player.y + self.offset_y + self.player.vy * lead_gain - self.y
        
        if not self.exploded:
            self.theta = atan2(-delta_y, delta_x) * 180/pi


    def update(self):
        
        # update position
        self.x += self.speed * cos(self.theta * pi/180)
        self.y -= self.speed * sin(self.theta * pi/180)
        
        # rotate the missile image
        self.image = pygame.transform.rotate(self.image0, self.theta)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
        
        self.check_collide()
        
        # see if inside screen, if not, explode
        if not self.screen_rect.contains(self.rect):
            # missile is out of screen.
            self.explode()
            
        
    def explode(self):
        # missile to explode
        self.image0 = pygame.image.load(ASSETS / 'explosion2.png')
        self.image0 = pygame.transform.rotate(self.image0, -90)
        if not self.exploded:
            # you have not exploded yet
            self.exploded = True
            self.explode_time = pygame.time.get_ticks()
            self.speed = 0
        
    def check_collide(self):
        # check for tank collision
        collided = pygame.sprite.collide_rect(self, self.player)
        
        if collided:
            self.explode()
            
        
        # missile AND tank to kill
        t_now = pygame.time.get_ticks()
        if self.exploded and (t_now - self.explode_time > self.kill_delay):
            # time to kill
            self.kill()
        
        
        
        