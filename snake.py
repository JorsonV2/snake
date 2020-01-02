import sys, pygame, random

pygame.init()

width = 600
height = 600
rows = 30
rectSize = 20
red = 255, 0, 0
black = 0, 0, 0
green = 0, 255, 0

size = width, height

screen  = pygame.display.set_mode(size)

class Line:
    def __init__(self, startPos, endPos):
        self.startPos = startPos
        self.endPos = endPos

    color = 255,255,255

class Grid:
    def __init__(self, numOfRows):
        for x in range(numOfRows):
            self.lines.append(Line([x * rectSize, 0], [x * rectSize, height]))
            self.lines.append(Line([0, x * rectSize],[width, x * rectSize]))

    lines = []

class Rect:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
    
    offset = 2

class Snake:
    def __init__(self, posX, posY):
        self.rects.append(Rect(posX, posY, green))

    def moveSnake(self):
        for x in range(1, len(self.rects)):
            self.rects[len(self.rects) - x].posX = self.rects[len(self.rects) - x - 1].posX
            self.rects[len(self.rects) - x].posY = self.rects[len(self.rects) - x - 1].posY

    def addRect(self, posX, posY):
        self.rects.append(Rect(posX, posY, green))

    def resetSnake(self):
        self.rects.clear()
        self.rects.append(Rect(10 * rectSize, 10 * rectSize, green))
        self.direction = 0, 1

    direction = 0, 1
    rects = []

class Apple:
    def newApple(self):
        self.rect = Rect(random.randint(0, rows -1) * rectSize, random.randint(0, rows - 1) * rectSize, red)
        for x in snake.rects:
            if x.posX == self.rect.posX and x.posY == self.rect.posY:
                newApple()

    rect = Rect(random.randint(0, rows - 1) * rectSize, random.randint(0, rows - 1) * rectSize, red)

def Game():

    # set tick of the game
    clock.tick_busy_loop(6 + len(snake.rects))

    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w and snake.direction[1] == 0:
                snake.direction = [0, -1]
            elif event.key == pygame.K_s and snake.direction[1] == 0:
                snake.direction = [0, 1]
            elif event.key == pygame.K_a and snake.direction[0] == 0:
                snake.direction = [-1, 0]
            elif event.key == pygame.K_d and snake.direction[0] == 0:
                snake.direction = [1, 0]

    # get last snake rect pos in case of colision with apple
    lastSnakeRectPos = [snake.rects[len(snake.rects) - 1].posX, snake.rects[len(snake.rects) - 1].posY]
    
    # move whole snake without head
    snake.moveSnake()

    # move snake head
    snake.rects[0].posX += snake.direction[0] * rectSize
    snake.rects[0].posY += snake.direction[1] * rectSize

    if snake.rects[0].posX > width - rectSize:
        snake.rects[0].posX = 0
    elif snake.rects[0].posX < 0:
        snake.rects[0].posX = width - rectSize
    
    if snake.rects[0].posY > height - rectSize:
        snake.rects[0].posY = 0
    elif snake.rects[0].posY < 0:
        snake.rects[0].posY = height - rectSize

    # check collision with apple
    if snake.rects[0].posX == apple.rect.posX and snake.rects[0].posY == apple.rect.posY:
        snake.addRect(lastSnakeRectPos[0], lastSnakeRectPos[1])
        apple.newApple()

    for x in range(1, len(snake.rects)):
        if snake.rects[0].posX == snake.rects[x].posX and snake.rects[0].posY == snake.rects[x].posY:
            snake.resetSnake()
            apple.newApple()
            break

    # display game
    screen.fill(black)

    for x in grid.lines:
        pygame.draw.line(screen, x.color, x.startPos, x.endPos)

    pygame.draw.rect(screen, apple.rect.color, [apple.rect.posX + apple.rect.offset, apple.rect.posY + apple.rect.offset, rectSize -  2 * apple.rect.offset + 1, rectSize -  2 * apple.rect.offset + 1])

    for x in snake.rects:
        pygame.draw.rect(screen, x.color, [x.posX + x.offset, x.posY + x.offset, rectSize - 2 * x.offset + 1, rectSize - 2 * x.offset + 1])

    pygame.display.flip()

grid = Grid(rows)
snake = Snake(10 * rectSize, 10 * rectSize)
apple = Apple()
Clock = pygame.time.Clock
clock = Clock()

while 1:

    Game()

    