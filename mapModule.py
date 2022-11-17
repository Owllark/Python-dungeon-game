import pygame

class Map:
    def __init__(self, width, height, cellSize):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.cellAmountW = int(width / cellSize)
        self.cellAmountH = int(height / cellSize)

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
                if self.cells[i][j] == 1:
                    activeColor = self.colorPurple

                pygame.draw.rect(display, activeColor, cell)

    def set_state(self, x, y, state):
        self.cells[x][y] = state

    def __del__(self):
        pass