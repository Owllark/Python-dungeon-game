import pygame
import random

class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Map:
    def __init__(self, width, height, cellSize):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.cellAmountW = int(width / cellSize)
        self.cellAmountH = int(height / cellSize)
        self.field = [False] * self.cellAmountW
        for i in range(0, self.cellAmountW):
            self.field[i] = [False] * self.cellAmountH
        visited = [False] * int(self.cellAmountW / 2)
        for i in range(0, int(self.cellAmountW / 2)):
            visited[i] = [False] * int(self.cellAmountH / 2)
        maze(0 ,0, self.cellAmountW, self.cellAmountH, self.field, visited)
        self.cells = [0] * self.cellAmountW
        for i in range(0, self.cellAmountW):
            self.cells[i] = [0] * self.cellAmountH

        self.colorPurple = (150, 30, 180)
        self.colorWhite = (255, 255, 255)
        self.colorDarkGrey = (25, 25, 25)

    def print_parameters(self):
        print(self.width, self.height)

    def draw(self, display):
        for i in range(0, self.cellAmountW):
            for j in range(0, self.cellAmountH):
                cell = pygame.Rect(i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize)
                activeColor = self.colorDarkGrey
                if self.field[i][j] == True:
                    activeColor = self.colorPurple

                pygame.draw.rect(display, activeColor, cell)

    def set_state(self, x, y, state):
        self.cells[x][y] = state

    def __del__(self):
        pass


def maze(x, y, cellAmountW, cellAmountH, field, visited):
    visited[x][y] = True
    field[2 * x + 1][2 * y + 1] = True
    n = [position(0, 0)] * 4
    n[0] = position(x - 1, y)
    n[1] = position(x, y - 1)
    n[2] = position(x + 1, y)
    n[3] = position(x, y + 1)

    for i in range(0, 4):
        idx = random.randint(0, 3)
        if idx != i:
            temp = n[idx]
            n[idx] = n[i]
            n[i] = temp

    for i in range(0, 4):
        temp = n[i]
        if temp.x >= 0 and temp.y >= 0 and temp.x < int(cellAmountW / 2) and temp.y < int(cellAmountH / 2):
            if not visited[temp.x][temp.y]:
                field[x*2 + (temp.x - x) + 1][y*2 + (temp.y - y) + 1] = True
                visited[temp.x][temp.y] = True
                maze(temp.x, temp.y, cellAmountW, cellAmountH, field, visited)
