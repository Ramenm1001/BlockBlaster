import pygame.draw
class Palma:
    def __init__(self, win, x, y, tall):
        self.x = x
        self.y = y
        self.win = win
        self.tall = tall
        self.color = [252, 169, 3]

    def draw(self):
        pygame.draw.rect(self.win,
                         self.color,
                         (self.x, self.y,
                          20, self.tall))
        pygame.draw.rect(self.win,
                         (0, 200, 15),
                         (self.x-10, self.y,
                          50, 20))

    def recolor(self):
        self.color[2] += 1
    def update(self):
        self.draw()
        self.recolor()
