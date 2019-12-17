import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((900, 500), 0, 32)

pygame.display.set_caption(" claswork - 1")
main_surface.fill((255, 255, 255))

space = 5
brick_with = (main_surface.get_width() - space * 10) / 9
x_pos = 5
for x in range(9):
    pygame.draw.rect(main_surface, (255, 0, 0), (x_pos, 490, brick_with, 5), 0)
    x_pos += space + brick_with


space = 5
brick_with = (main_surface.get_width() - space * 10) / 9
x_pos = brick_with + space * 2
for x in range(7):
    pygame.draw.rect(main_surface, (255, 153, 13), (x_pos, 480, brick_with, 5), 0)
    x_pos += space + brick_with


space = 5
brick_with = (main_surface.get_width() - space * 10) / 9
x_pos = brick_with * 2 + space * 3
for x in range(5):
    pygame.draw.rect(main_surface, (255, 255, 0), (x_pos, 470, brick_with, 5),0)
    x_pos += space + brick_with


space = 5
brick_with = (main_surface.get_width() - space * 10) / 9
x_pos = brick_with * 3 + space * 4
for x in range(3):
    pygame.draw.rect(main_surface, (0, 255, 0), (x_pos, 460, brick_with, 5), 0)
    x_pos += space + brick_with


space = 5
brick_with = (main_surface.get_width() - space * 10) / 9
x_pos = brick_with * 4 + space * 5
for x in range(1):
    pygame.draw.rect(main_surface, (0, 255, 255), (x_pos, 450, brick_with, 5), 0)
    x_pos += space + brick_with
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()