import pygame

class HealthBar():
    def __init__(self):
        self.w = 120
        self.h = 20
        self.image = pygame.Surface((self.w, self.h))
        # make it red
        self.red = (255,50,50)
        self.green = (50,255,50)
        self.image.fill(self.red)
        self.rect = self.image.get_rect()
        self.health = 100 # percent
        self.font = pygame.font.Font(size=22)
        self.title = self.font.render("Health", 1, (0,0,0))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.rect.center
        print(self.title)
        
        
        self.update()

    
    def increment(self,amount):
        # decrement tanks health
        if self.health + amount <= 0:
            self.health = 0
        else:
            print(self.health)
            self.health += amount
        
        self.update()
    
    def update(self):
        # set the green amount on bar
        green_w = self.health/100 * self.w
        green_h = self.h
        # draw red
        self.image.fill(self.red)
        # draw green
        green_image = pygame.Surface((green_w,green_h))
        green_image.fill(self.green)
        # blit green image onto self.image
        self.image.blit(green_image,(0,0))
        # blit the title over it all
        self.image.blit(self.title, self.title_rect)
        
