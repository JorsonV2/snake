import sys, pygame

pygame.init()

width = 500
height = 500
rows = 50
rectSize = 10
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
        for x in range(numOfRows + 1):
            self.lines.append(Line([x * rectSize, 0], [x * rectSize, height]))
            self.lines.append(Line([0, x * rectSize],[width, x * rectSize]))

    lines = []

class Rect:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
    
    offset = 1

class Snake:
    def __init__(self, posX, posY):
        self.rects.append(Rect(posX, posY, green))

    direction = 0, 1
    rects = []

def Game():

    clock.tick_busy_loop(10)

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

    snake.rects[0].posX += snake.direction[0] * rectSize
    snake.rects[0].posY += snake.direction[1] * rectSize

    if snake.rects[0].posX > width:
        snake.rects[0].posX = 0
    elif snake.rects[0].posX < 0:
        snake.rects[0].posX = width
    
    if snake.rects[0].posY > height:
        snake.rects[0].posY = 0
    elif snake.rects[0].posY < 0:
        snake.rects[0].posY = height

    screen.fill(black)

    for x in grid.lines:
        pygame.draw.line(screen, x.color, x.startPos, x.endPos)

    for x in snake.rects:
        pygame.draw.rect(screen, x.color, [x.posX + x.offset, x.posY + x.offset, rectSize - x.offset, rectSize - x.offset])

    pygame.display.flip()

    

grid = Grid(rows)
snake = Snake(10 * rectSize, 10 * rectSize)
Clock = pygame.time.Clock
clock = Clock()


while 1:

    Game()

    