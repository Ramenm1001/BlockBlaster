import pygame
from negr import Negr
from palma import Palma
from housefornigga import HouseNigga

win = pygame.display.set_mode((500, 500))
negr = Negr(win, 200, 400, 50)
palma = Palma(win, 250,444,55 )

island = [negr, ]
run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    for some in island:
        some.draw()
    pygame.display.update()
pygame.quit()
