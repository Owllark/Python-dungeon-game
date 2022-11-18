import pygame
import random
import engine
import copy


class Dungeon:
    def __init__(self, mapScale, screenW, screenH, cellAmountW, cellAmountH):
        self.mapScale = mapScale
        self.maxX = screenW * mapScale
        self.maxY = screenH * mapScale
        self.cellAmountH = cellAmountH
        self.cellAmountW = cellAmountW
        self.screenCenter = engine.position(int(screenW / 2), int(screenH / 2))
        self.cameraPos = copy.copy(self.screenCenter)
        self.cellSize = int((screenW / cellAmountW) * mapScale)
        self.field = [False] * cellAmountW

        self.visibility = int(cellAmountW / mapScale) + 1

        # initialize field data
        for i in range(0, cellAmountW):
            self.field[i] = [False] * cellAmountH
        # temporary array for maze generation
        visited = [False] * int(cellAmountW / 2)
        for i in range(0, int(cellAmountW / 2)):
            visited[i] = [False] * int(cellAmountH / 2)
        # maze generation
        maze(0 ,0, cellAmountW, cellAmountH, self.field, visited)

    def draw(self, display):
        curCell = engine.position(int(self.cameraPos.x / self.cellSize), int(self.cameraPos.y / self.cellSize))
        # print(self.cameraPos.x, self.cameraPos.y)
        for i in range(curCell.x - self.visibility, curCell.x + self.visibility):
            for j in range(curCell.y - 3, curCell.y + 3):
                deltaPos = engine.position(self.screenCenter.x - self.cameraPos.x, self.screenCenter.y - self.cameraPos.y)
                cell = pygame.Rect(i * self.cellSize + deltaPos.x, j * self.cellSize + deltaPos.y, self.cellSize, self.cellSize)
                activeColor = engine.darkGrey
                if self.field[i][j] == True:
                    activeColor = engine.purple

                pygame.draw.rect(display, activeColor, cell)

    def set_state(self, x, y, state):
        self.cells[x][y] = state

    def __del__(self):
        pass


def maze(x, y, cellAmountW, cellAmountH, field, visited):
    visited[x][y] = True
    field[2 * x + 1][2 * y + 1] = True
    n = [engine.position(0, 0)] * 4
    n[0] = engine.position(x - 1, y)
    n[1] = engine.position(x, y - 1)
    n[2] = engine.position(x + 1, y)
    n[3] = engine.position(x, y + 1)

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
