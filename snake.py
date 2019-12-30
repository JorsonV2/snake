import sys, pygame

pygame.init()

width = 501
height = 501
rows = 20
rectSize = 25
red = 255, 0, 0
black = 0, 0, 0
rect = pygame.Rect(100, 100, 150, 150)

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

grid = Grid(rows)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for x in grid.lines:
        pygame.draw.line(screen, x.color, x.startPos, x.endPos)

    pygame.display.flip()