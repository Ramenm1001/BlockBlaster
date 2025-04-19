import pygame.draw


class Negr:
    def __init__(self, win, x, y, tall):
        self.win = win
        self.x = x
        self.y = y
        self.tall = tall
        self.d = 1

    def draw(self):
        pygame.draw.rect(self.win,
                         (170, 100, 15),
                         (self.x, self.y,
                          20, self.tall))

    def run(self):
        if self.d == 1:
            self.x += 1
            if self.x > 500:
                self.d = -1
        else:
            self.x -= 1
            if self.x < 0:
                self.d = 1

    def update(self):
        self.draw()



