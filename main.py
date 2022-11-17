import pygame
import mapModule
import creatureModule as creature

aimSin = 0;
aimCos = 0;

def draw_eyes(centerX, centerY, mX, mY, radius):
    leftX = centerX - 2*radius
    leftY = centerY
    rightX = centerX + 2 * radius
    rightY = centerY
    global aimSin
    global aimCos
    if centerX - mX == 0:
        aimSin = 0
    else:
        aimSin = -(centerX - mX) / ((centerX - mX) ** 2 + (centerY - mY) ** 2) ** (1 / 2)
    if centerY- mY == 0:
        aimCos = 1
    else:
        aimCos = -(centerY - mY) / ((centerX - mX) ** 2 + (centerY - mY) ** 2) ** (1 / 2)

    pygame.draw.circle(display, (50, 10, 10), (centerX, centerY), radius * 4)
    pygame.draw.circle(display, white, (leftX, leftY), radius)
    pygame.draw.circle(display, white, (rightX, rightY), radius)
    if leftX - mX == 0:
        sinL = 0
    else:
        sinL = -(leftX - mX) / ((leftX - mX) ** 2 + (leftY - mY) ** 2) ** (1 / 2)
    if leftY - mY == 0:
        cosL = 1
    else:
        cosL = -(leftY - mY) / ((leftX - mX) ** 2 + (leftY - mY) ** 2) ** (1 / 2)
    pXL = leftX + int((radius / 2) * sinL)
    pYL = leftY + int((radius / 2) * cosL)
    pygame.draw.circle(display, black, (pXL, pYL), int(radius / 2))

    if rightX - mX == 0:
        sinR = 0
    else:
        sinR = -(rightX - mX) / ((rightX - mX) ** 2 + (rightY - mY) ** 2) ** (1 / 2)
    if rightY - mY == 0:
        cosR = 1
    else:
        cosR = -(rightY - mY) / ((rightX - mX) ** 2 + (rightY - mY) ** 2) ** (1 / 2)
    pXR = rightX + int((radius / 2) * sinR)
    pYR = rightY + int((radius / 2) * cosR)
    pygame.draw.circle(display, black, (pXR, pYR), int(radius / 2))


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
purple = (150, 30, 180)

width = 1920
height = 1080
cellSize = 40

display = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

game_over = False

x = width / 2
y = height / 2
pos = (x, y)

lifes = 3
squareSpeed = 10
monsterSpeed = 5
monsterX = width / 2
monsterY = height / 2

square = creature.MainCharacter(x - 15 * cellSize, y, squareSpeed, cellSize, lifes)
mainMap = mapModule.Map(width, height, cellSize)
pressedKey = [False] * 1024
mousePressed = False
mX = width / 2
mY = height / 2
while not game_over:
    display.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            mX = pos[0]
            mY = pos[1]
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
    #pygame.draw.rect(display, purple, rect)
    leftEyeX = mX - 50
    leftEyeY = mY
    rightEyeX = mX + 50
    rightEyeY = mY
    monsterX += int(aimSin * monsterSpeed)
    monsterY += int(aimCos * monsterSpeed)
    draw_eyes(monsterX, monsterY, square.x, square.y, 30)
    square.draw(display)
    #prightX = int((mX + rightX) / 2)
    #prightY = int((mY + rightY) / 2)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()



