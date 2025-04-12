import pygame
from negr import Negr
from palma import Palma

win = pygame.display.set_mode((500, 500))


run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    pygame.display.update()
pygame.quit()
