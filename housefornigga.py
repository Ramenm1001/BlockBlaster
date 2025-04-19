import pygame.draw
class HouseNigga:
    def __init__(self, win, x, y, tall):
        self.win = win
        self.x = x
        self.y = y
        self.tall = tall

    def draw(self):
        pygame.draw.rect(self.win, (170, 100, 15), (self.x, self.y, 100, self.tall))
        pygame.draw.rect(self.win, (150, 112, 10), (self.x - 5, self.y - 10, 110, 10))
        pygame.draw.rect(self.win, (24, 64, 252), (self.x + 9, self.y + 6, 20, 20))
        pygame.draw.rect(self.win, (24, 64, 252), (self.x + 72, self.y + 6, 20, 20))
    def recolor(self):
        pass

    def update(self):
        self.draw()
