import pygame
from background import Background
from tank import Tank
from rock import Rock
pygame.init()
pygame.font.init()


import gif_pygame

TS = 64
SIZE = (11*TS, 8*TS)
# make our screen
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


animation_gif = gif_pygame.load("yes.gif")
gif_pygame.transform.rotozoom(animation_gif, 0, 0.2)

# make some rocks
rocks = pygame.sprite.Group()
missiles = pygame.sprite.Group()


# make tank at center of screen
tank = Tank(*[s//2 for s in SIZE], rocks, screen)

# build actual tiled bg
bg_size = (11 * TS, 8 * TS)
bg = Background(bg_size,TS,tank)
bg.make_bg()


# add 15 rocksif self.x <=0:
num_rocks = [10]
for i in range(num_rocks[0]):
    new_rock = Rock(SIZE,num_rocks,tank,missiles,screen)
    # check and see if new rock collides with player
    rocks.add(new_rock)


score = 100
# make my font
f = pygame.font.Font('RubikDistressed-Regular.ttf', size=40)

# main game loop
active = True
while active:
    screen.fill((0,0,0))
    bg.draw(screen)
    # draw score
    # do rock stuff
    rocks.update()
    rocks.draw(screen)
    
    tank.update()
    tank.draw(screen)
    
    missiles.update()
    missiles.draw(screen)
    
    # check for collision
    #collided_rocks = pygame.sprite.spritecollide(tank,rocks,0)
    #for cr in collided_rocks:
    #   cr.explode()
    
    for i in range(len(rocks)-1,num_rocks[0]):
        rocks.add(Rock(SIZE,num_rocks,tank, missiles, screen))
    
      
    ##############
    animation_gif.render(screen, (10, 10))
    # add in score
    score-=1/60
    score_surface = f.render(f"{score:0.0f}", 1, (255,0,0))
    screen.blit(score_surface,(SIZE[0]-100, 30))

    pygame.display.flip()
    # get events
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            active = False
    clock.tick(60)
    # get fps
    fps = clock.get_fps()
    pygame.display.set_caption(f"{fps:0.1f}")
    
pygame.quit()
            