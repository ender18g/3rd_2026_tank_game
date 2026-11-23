import pygame
from math import atan2, pi, sin, cos
from healthbar import HealthBar
from random import uniform

class Tank(pygame.sprite.Sprite):
    def __init__(self,x,y, rocks, screen):
        pygame.sprite.Sprite.__init__(self)
        self.fp = r"kenney_top-down-tanks-remastered\PNG\Default size\tank_red.png"
        self.image = pygame.image.load(self.fp)
        # rotate 180
        self.image = pygame.transform.rotate(self.image,90)
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 0
        self.ds = 0.1
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.t_shot = 0 # the last time i shot a missile
        self.phi = 0 # angle of tank in deg
        self.rocks = rocks
        self.ammo = 0
        self.ammo_delay = 1000 # in ms, delay before i get ammo again
        self.t_ammo = 0 # last time that i got ammo
        # healthbar
        self.hb = HealthBar()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.d_fwd = 50 # look 100 pixels forward
        self.fwd_rect = pygame.Rect(self.x, self.y, 10, 10)
        self.fwd_surf = pygame.Surface((10,10))
        self.fwd_surf.fill((0,0,255))
    
    def update(self):
        self.x += self.speed * cos(self.phi * pi/180)
        self.y -= self.speed * sin(self.phi * pi/180)
        
        self.rect.center = (self.x, self.y)
        
        self.check_keys()
        
        self.check_rocks()
        
        # there is a small chance, we lose health
        if uniform(0,100)<3:
            self.hb.increment(-2)
            
        # check if inside of screen else stop
        #if not self.screen_rect.contains(self.rect):
        #   self.x, self.y = self.screen_rect.center
        
        # look forward of the tank, then check for collision
        fwd_x = self.x + 70 * cos(self.phi * pi/180)
        fwd_y = self.y - 70 * sin(self.phi * pi/180)
        self.fwd_rect.center = (fwd_x, fwd_y)
        
        if not self.screen_rect.contains(self.fwd_rect):
            print('tank out of screen')
            self.speed = 0
        
    
    def check_rocks(self):
        # if i hit a rock. stop.
        collided_rocks = pygame.sprite.spritecollide(self, self.rocks,0)
        
        t_now = pygame.time.get_ticks()
        
        if collided_rocks and t_now-self.t_ammo >self.ammo_delay:
            self.ammo +=1
            self.t_ammo = t_now
        
    def shoot(self):
        # make a bullet
        pass
        # new_bullet = Bullet(self.x,self.y)
        
    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed +=self.ds
        if keys[pygame.K_DOWN]:
            self.speed -=self.ds
        if keys[pygame.K_LEFT]:
            self.phi += 1
        if keys[pygame.K_RIGHT]:
            self.phi -= 1 
   
    def draw(self,screen):
        # rotate image based on velocity
        rot_image = pygame.transform.rotate(self.image, self.phi)
        self.rect = rot_image.get_rect(center=(self.x,self.y))
        #always draw to the center of the screen
        screen.blit(rot_image, self.rect)
        
        # now blit the health bar
        self.hb.rect.midtop = self.rect.midbottom
        self.hb.rect.y += 10
        screen.blit(self.hb.image, self.hb.rect)
        
        # now blit the fwd rect
        screen.blit(self.fwd_surf, self.fwd_rect)
        
        
        
        
        
        
        
        
        