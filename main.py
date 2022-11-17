import pygame
import dungeon
import creature_module as creature
import engine


game_over = False
pressedKey = [False] * 1024
mousePressed = False
mousePos = engine.position(0, 0)


def event_handler():
    global game_over
    global pressedKey
    global mousePressed
    global mousePos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            mousePos.x = pos[0]
            mousePos.y = pos[1]
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

# aim for Ilya Eye Monster
aimSin = 0;
aimCos = 0;


# draw Ilya EyeMonster that looks to the given point
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
    pygame.draw.circle(display, engine.white, (leftX, leftY), radius)
    pygame.draw.circle(display, engine.white, (rightX, rightY), radius)
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
    pygame.draw.circle(display, engine.black, (pXL, pYL), int(radius / 2))

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
    pygame.draw.circle(display, engine.black, (pXR, pYR), int(radius / 2))


pygame.init()

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
monsterPos = engine.position(width / 2, height / 2)

square = creature.MainCharacter(x - 15 * cellSize, y, squareSpeed, cellSize, lifes)
mainMap = dungeon.Dungeon(1.0, width, height, 96, 54)
mX = width / 2
mY = height / 2
while not game_over:
    display.fill(engine.white)
    event_handler()

    # movement of main character
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

    # drawing
    rect = pygame.Rect(mousePos.x - cellSize / 2 - 100, mousePos.y - cellSize / 2 - 100, cellSize, cellSize)
    mainMap.draw(display)
    pygame.draw.rect(display, engine.purple, rect)

    monsterPos.x += int(aimSin * monsterSpeed)
    monsterPos.y += int(aimCos * monsterSpeed)
    draw_eyes(monsterPos.x, monsterPos.y, square.x, square.y, 30)
    square.draw(display)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()



