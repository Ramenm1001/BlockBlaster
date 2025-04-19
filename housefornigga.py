import pygame.draw
class HouseNigga:
    def __init__(self, win, x, y, tall):
        self.win = win
        self.x = x
        self.y = y
        self.tall = tall

    def draw(self):
        pygame.draw.rect(self.win, (170, 100, 15), (self.x, self.y, 100, self.tall))
        pygame.draw.rect(self.win, (10, 100, 15), (self.x, self.y-10, 10, self.tall))
    def recolor(self):
        pass

    def update(self):
        self.draw()
