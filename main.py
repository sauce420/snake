#I guess I'll do this in a less object oriented way because
#there are loads of object-oriented snakes out there
import pygame

pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
width = 500
x1 = 250
y1 = 250
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, width))
pygame.display.set_caption('Snake, use the arrow keys to move around, press escape to close')

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)
        
    x1 += x1_change
    y1 += y1_change
    win.fill(BLACK)
    pygame.draw.rect(win,WHITE,[x1,y1,10,10])

    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()
