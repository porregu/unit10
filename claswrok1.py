import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((600, 500), 0, 32)

pygame.display.set_caption(" claswork - 1")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface,(0, 255, 0), ((300, 50), (400, 100), (375, 200), (250, 200), (200, 100)), 0)
pygame.draw.line(main_surface,())


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()