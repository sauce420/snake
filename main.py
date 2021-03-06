#I guess I'll do this in a less object oriented way because
#there are loads of object-oriented snakes out there
import pygame
from time import sleep


pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
width = 500
font_style = pygame.font.SysFont(None, 50)
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
                loop = False
    if x1 >= width or x1 < 0 or y1 >= width or y1 < 0:
        loop = False

    x1 += x1_change
    y1 += y1_change
    win.fill(BLACK)
    pygame.draw.rect(win,WHITE,[x1,y1,10,10])

    pygame.display.update()

    clock.tick(30)
mesg = font_style.render("You lost", True, WHITE)
win.blit(mesg, [width/2, width/2])
pygame.display.update()
print("You lost (collision with edge)")
sleep(2)
pygame.quit()
quit()
