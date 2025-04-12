import pygame


class Player:
    def __init__(self):
        pass

    def draw(self):
        pass

    def move(self):
        pass

    def update(self):
        pass


class Bullet:
    def __init__(self):
        pass

    def draw(self):
        pass

    def move(self):
        pass

    def update(self):
        pass


win = pygame.display.set_mode((500, 500))

run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    pygame.display.update()
pygame.quit()
