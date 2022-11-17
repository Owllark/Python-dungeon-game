import pygame
import mapModule
import creatureModule as creature

pygame.init()

white = (255, 255, 255)
purple = (150, 30, 180)

width = 640
height = 400
cellSize = 10

display = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

game_over = False

x = width / 2
y = height / 2
pos = (x, y)

lifes = 3

square = creature.MainCharacter(x - 3 * cellSize, y, 1, 2 * cellSize, 3)
mainMap = mapModule.Map(width, height, cellSize)
pressedKey = [False] * 1024;
mousePressed = False

while not game_over:
    display.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousePressed = False

        if event.type == pygame.KEYDOWN:
            #in real game should be deleted
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_a:
                pressedKey[pygame.K_a] = True
            elif event.key == pygame.K_d:
                pressedKey[pygame.K_d] = True
            elif event.key == pygame.K_w:
                pressedKey[pygame.K_w] = True
            elif event.key == pygame.K_s:
                pressedKey[pygame.K_s] = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                pressedKey[pygame.K_a] = False
            elif event.key == pygame.K_d:
                pressedKey[pygame.K_d] = False
            elif event.key == pygame.K_w:
                pressedKey[pygame.K_w] = False
            elif event.key == pygame.K_s:
                pressedKey[pygame.K_s] = False

    # movement
    if pressedKey[pygame.K_a]:
        square.move(creature.DIRECTION.LEFT)
    if pressedKey[pygame.K_d]:
        square.move(creature.DIRECTION.RIGHT)
    if pressedKey[pygame.K_w]:
        square.move(creature.DIRECTION.UP)
    if pressedKey[pygame.K_s]:
        square.move(creature.DIRECTION.DOWN)

    if mousePressed:
        mainMap.set_state(int(pos[0] / cellSize), int(pos[1] / cellSize), 1)


    rect = pygame.Rect(pos[0] - cellSize / 2, pos[1] - cellSize / 2, cellSize, cellSize)
    mainMap.draw(display)
    square.draw(display)
    pygame.draw.rect(display, purple, rect)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()



