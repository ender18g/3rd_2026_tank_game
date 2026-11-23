import pygame
from pathlib import Path


class Background():
    def __init__(self,size,ts,player):
        ASSETS = Path(r"kenney_top-down-tanks-remastered\PNG\Default size")
        g_fp = ASSETS / "tileGrass1.png"
        s_fp = ASSETS / "tileSand1.png"
        
        b_fp = r"kenney_top-down-tanks-remastered\PNG\Default size\tileGrass_transitionE.png"
        gr_fp = r"kenney_top-down-tanks-remastered\PNG\Default size\tileGrass_roadNorth.png"
        sr_fp = r"kenney_top-down-tanks-remastered\PNG\Default size\tileSand_roadNorth.png"
        
        g = pygame.image.load(g_fp)
        s = pygame.image.load(s_fp)
        b = pygame.image.load(b_fp)
        gr = pygame.image.load(gr_fp)
        sr = pygame.image.load(sr_fp)
        
        self.tile_matrix = [
                [g, g, gr, g, g, b, s, s, sr, s, s],
                [g, g, gr, g, g, b, s, s, sr, s, s],
                [g, g, gr, g, g, b, s, s, sr, s, s],
                [g, g, gr, g, g, b, s, s, sr, s, s],
                [g, g, gr, g, g, b, s, s, sr, s, s],
                [g, g, gr, g, g, b, s, s, sr, s, s],
                [g, g, gr, g, g, b, s, s, s, s, s],
                [g, g, gr, g, g, b, s, s, s, s, s]         
            ]
        
        self.size = size
        self.ts = ts
        self.player = player
        
        self.i = 0
        
    def make_bg(self):
        # make the big bg surface
        self.bg = pygame.Surface(self.size)
        
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                # blit the tile on the bg surface
                self.bg.blit(self.tile_matrix[r][c], (c*self.ts, r*self.ts), )
        
        self.rect = self.bg.get_rect()
        return self.bg
    

    def draw(self,screen):
        # get offset
        #offset_x = (screen.get_width() // 2) - self.player.rect.centerx
        #offset_y = (screen.get_height() // 2) - self.player.rect.centery

        # blit the background shifted by that offset
        screen.blit(self.bg, (0, 0))
    
        
        
        
        
        