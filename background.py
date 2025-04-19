import pygame.draw
class HouseNigga:
    def __init__(self, win, x, y, tall):
        self.win = win
        self.x = x
        self.y = y
        self.tall = tall

    def draw(self):
        pygame.draw.rect(self.win, (9, 145, 12), (self.x, self.y, 1000, 1000))
        pygame.draw.rect(self.win, (9, 145, 12), (self.x, self.y-200, 1000, 1000))




    def recolor(self):
        pass

    def update(self):
        self.draw()