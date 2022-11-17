import pygame
from enum import Enum
import engine


# синтаксис класса
class DIRECTION(Enum):
    DOWN = 1
    UP = 2
    RIGHT = 3
    LEFT = 4


class Creature:

    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size

    def __del__(self):
        pass

    def move(self, direction):
        if direction == DIRECTION.DOWN:
            self.y += self.speed
        if direction == DIRECTION.UP:
            self.y -= self.speed
        if direction == DIRECTION.RIGHT:
            self.x += self.speed
        if direction == DIRECTION.LEFT:
            self.x -= self.speed
        pass

    def draw(self):
        pass


class MainCharacter(Creature):
    color = (255, 255, 255)
    def __init__(self, x, y, speed, size, lifes):
        Creature.__init__(self, x, y, speed, size)
        self.lifes = lifes

    def draw(self, display):
        rect = pygame.Rect(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)
        pygame.draw.rect(display, self.color, rect)
