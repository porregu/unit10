import pygame, sys
from pygame.locals import *
import random

pygame.init()

main_surface = pygame.display.set_mode((1000, 800), 0, 32)

pygame.display.set_caption(" claswork - 2")
main_surface.fill((0, 76, 103))
pygame.draw.circle(main_surface, (255, 255, 0), (100, 100), 50, 0)
for x in range(24):
    random1 = random.randint(10, 1000)
    random3 = random.randint(10, 800)
    pygame.draw.circle(main_surface, (255, 255, 255), (random1, random3), 5, 0)
pygame.draw.polygon(main_surface,(0, 255, 0), ((0, 800), (0, 150), (50, 100), (150, 100), (150, 150), (40, 150), (40, 200), (100, 200), (100, 250), (200, 250), (200, 300), (20, 300), (20, 350), (40, 350), (40, 400), (175, 400), (175, 600), (60, 600), (60, 700), (0, 700), (0, 800)), 0)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()