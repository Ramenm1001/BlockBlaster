import pygame.draw
import random


class Fire:
    def __init__(self, win, x, y):
        self.x = x
        self.y = y
        self.win = win
        self.color1 = [200, 50, 50]
        self.color2 = [200, 50, 50]
        self.color3 = [200, 50, 50]
        self.parts = []

    def draw(self):
        pygame.draw.rect(self.win,
                         self.color1,
                         (self.x, self.y,
                          20, 20))
        pygame.draw.rect(self.win,
                         self.color2,
                         (self.x, self.y - 5,
                          20, 20))
        pygame.draw.rect(self.win,
                         self.color3,
                         (self.x, self.y - 10,
                          20, 20))
        for part in self.parts[:]:
            part.update()
            if part.timer <= 0:
                self.parts.remove(part)

    def recolor(self):
        self.color1 = [random.randint(170, 255), random.randint(200, 235), random.randint(0, 50)]
        self.color2 = [random.randint(200, 255), random.randint(150, 155), random.randint(0, 50)]
        self.color3 = [random.randint(200, 255), random.randint(150, 155), random.randint(0, 50)]

    def add_parts(self):
        self.parts.append(Part(self.win, self.x + 10, self.y + 10, random.choice([self.color1, self.color2, self.color3])))

    def update(self):
        self.draw()
        self.recolor()
        self.add_parts()


class Part:
    def __init__(self, win, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.win = win
        self.timer = 50
        self.size = 5

    def draw(self):
        pygame.draw.rect(self.win,
                         self.color,
                         (self.x, self.y,
                          self.size, self.size))
    def recolor(self):
        for i in range(3):
            self.color[i] -= 1
            if self.color[i] < 150:
                self.color[i] = 150

    def update(self):
        self.draw()
        self.recolor()
        self.timer -= 1
        self.x += random.randint(0, 4) - 2
        self.y -= random.randint(0, 10)
        self.size += 40 // max(10, self.timer)