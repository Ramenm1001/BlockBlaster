import pygame.draw
class Sun:
    def __init__(self, win, x, y, tall):
        self.x = x
        self.y = y
        self.win = win
        self.tall = tall
        self.color = [255, 255, 0]
        self.speed = 10

    def draw(self):
        pygame.draw.rect(self.win,
                         self.color,
                         (self.x, self.y,
                          20, self.tall))
        pygame.draw.rect(self.win,
                         (255, 200, 15),
                         (self.x-10, self.y,
                          100, 100))


    def cordx(self):
        self.x -= self.speed
        if self.x <= 0:
            self.speed *= -1
        if self.x + 100 >= 500:
            self.speed *= -1

    def update(self):
        self.draw()
        self.cordx()
