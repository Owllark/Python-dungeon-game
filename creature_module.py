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

    def __init__(self, startX, startY, speed, size):
        self.x = startX
        self.y = startY
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

    def __init__(self, startX, startY, drawPosX, drawPosY, speed, size, lifes):
        Creature.__init__(self, startX, startY,  speed, size)
        self.lifes = lifes
        self.drawPos = engine.position(drawPosX, drawPosY)

    def draw(self, display):
        rect = pygame.Rect(self.drawPos.x - self.size / 2, self.drawPos.y - self.size / 2, self.size, self.size)
        pygame.draw.rect(display, engine.white, rect)
