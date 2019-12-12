import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((600, 500), 0, 32)

pygame.display.set_caption(" claswork - 1")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface,(0, 255, 0), ((300, 50), (400, 100), (375, 200), (250, 200), (200, 100)), 0)
pygame.draw.line(main_surface,(0, 0, 255), (255, 80), (305, 80), 5)
pygame.draw.line(main_surface,(0, 0, 255), (305, 80), (255, 100), 1)
pygame.draw.line(main_surface,(0, 0, 255), (255, 100), (305, 100), 5)
pygame.draw.rect(main_surface, (255, 0, 0), (320, 125, 100, 50),0)
pygame.draw.circle(main_surface, (0, 0, 255), (400, 50), 12, 0)
pygame.draw.ellipse(main_surface,( 255, 10, 0), (400, 200, 40, 70),2)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()