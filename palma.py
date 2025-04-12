import pygame.draw
class Palma:
    def __init__(self, win, x, y, tall):
        self.win = win
        self.x = x
        self.y = y
        self.tall = tall

    def draw(self):
        pygame.draw.rect(self.win,
                         (170, 100, 15),
                         (self.x, self.y,
                          20, self.tall))