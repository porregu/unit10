import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()