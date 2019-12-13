import pygame, sys
from pygame.locals import *
import random

pygame.init()

main_surface = pygame.display.set_mode((600, 800), 0, 32)

pygame.display.set_caption(" claswork - 2")
main_surface.fill((0, 76, 103))
pygame.draw.circle(main_surface, (255, 255, 0), (100, 100), 50, 0)
for x in range(24):
    random1 = random.randint(10, 600)
    random3 = random.randint(10, 800)
    pygame.draw.circle(main_surface, (255, 255, 255), (random1, random3), 5, 0)
pygame.draw.rect(main_surface, (0, 0, 0), (0, 650, 50, 250),0)
pygame.draw.rect(main_surface, (0, 0, 0), (50, 425, 75, 375),0)
pygame.draw.rect(main_surface, (0, 0, 0), (100, 675, 75, 225),0)
pygame.draw.rect(main_surface, (0, 0, 0), (175, 625, 100, 275),0)
pygame.draw.rect(main_surface, (0, 0, 0), (250, 350, 125, 450),0)
pygame.draw.rect(main_surface, (0, 0, 0), (350, 700, 100, 200),0)
pygame.draw.rect(main_surface, (0, 0, 0), (450, 575, 75, 325),0)
pygame.draw.rect(main_surface, (0, 0, 0), (500, 425, 75, 375),0)
pygame.draw.rect(main_surface, (0, 0, 0), (550, 550, 50, 350),0)
pygame.draw.rect(main_surface, (255, 255, 51), (60, 550, 15, 15),0)
pygame.draw.rect(main_surface, (255, 255, 51), (80, 500, 15, 15),0)
pygame.draw.rect(main_surface, (255, 255, 51), (65, 750, 15, 15),0)
pygame.draw.rect(main_surface, (255, 255, 51), (90, 750, 15, 15),0)
pygame.draw.rect(main_surface, (255, 255, 51), (575, 650, 15, 15),0)
pygame.draw.ellipse(main_surface,( 160, 160, 160), (150, 475, 300, 800),20)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()