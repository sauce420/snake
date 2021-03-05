import sys
import pygame
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Snake')

while True:
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit() 
