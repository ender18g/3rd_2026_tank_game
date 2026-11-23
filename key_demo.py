import pygame

pygame.init()

TS = 64
SIZE = (4*TS, 4*TS)
# make our screen
screen = pygame.display.set_mode(SIZE)
screen.fill((100,100,200))
clock = pygame.time.Clock()



# main game loop
active = True
while active:
    pygame.display.flip()
    # get events
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            active = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print('UP')
pygame.quit()
            
