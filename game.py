import pygame
import Objects
White = (255, 255, 255)
Black = (0, 0, 0)


def turn(white, black, rows):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            po = pygame.mouse.get_pos()
            isTouching(white, black, po, rows)
        if event.type == pygame.QUIT:
            quit()


def isTouching(white, black, po, rows):
    for i in white:
        for x in range(i.size):
            if i.pos[0]*i.dis + x == po[0]:
                for t in range(i.size):
                    if i.pos[1]*i.dis + t == po[1]:
                        print('escape to select different unit')
                        h = True
                        while h:
                            ti = pygame.key.get_pressed()
                            po2 = po
                            po = findPos(white, black, rows, po)
                            if po != po2:
                                h = False
                                # print(i.pos)
                                print(i.type)
                                i.move(white, black, po)
                            elif ti[pygame.K_ESCAPE]:
                                h = False

    for i in black:
        for x in range(i.size):
            if i.pos[0]*i.dis + x == po[0]:
                for t in range(i.size):
                    if i.pos[1]*i.dis + t == po[1]:
                        print('escape to select different unit')
                        h = True
                        while h:
                            ti = pygame.key.get_pressed()
                            po2 = po
                            po = findPos(white, black, rows, po)
                            if po != po2:
                                h = False
                            elif ti[pygame.K_ESCAPE]:
                                h = False


def findPos(white, black, rows, po):
    events = events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            po = pygame.mouse.get_pos()
            c = po[0] // rows
            v = po[1] // rows
            po = (c, v)
            return po
        if event.type == pygame.QUIT:
            quit()
    return po


def redrawWindow(white, black, win, width):
    win.fill((205, 127, 50))
    for i in range(len(white)):
        white[i].draw(win)
    for i in range(len(black)):
        black[i].draw(win)
    drawGrid(width, 8, win)
    pygame.display.update()


def drawGrid(w, rows, surface):
    SBT = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + SBT
        y = y + SBT

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def createList(width, rows):
    white = []
    black = []
    # for i in range(8):
    #     white.append(Objects.pawn(White, (i, 1), rows, width))
    #     black.append(Objects.pawn(Black, (i, 6), rows, width))
    white.append(Objects.rook(White, (0, 0), rows, width))
    white.append(Objects.rook(White, (7, 0), rows, width))
    white.append(Objects.knight(White, (1, 0), rows, width))
    white.append(Objects.knight(White, (6, 0), rows, width))
    white.append(Objects.bishop(White, (2, 0), rows, width))
    white.append(Objects.bishop(White, (5, 0), rows, width))
    white.append(Objects.queen(White, (3, 0), rows, width))
    white.append(Objects.king(White, (4, 0), rows, width))
    black.append(Objects.rook(Black, (0, 7), rows, width))
    black.append(Objects.rook(Black, (7, 7), rows, width))
    black.append(Objects.knight(Black, (1, 7), rows, width))
    black.append(Objects.knight(Black, (6, 7), rows, width))
    black.append(Objects.bishop(Black, (2, 7), rows, width))
    black.append(Objects.bishop(Black, (5, 7), rows, width))
    black.append(Objects.queen(Black, (4, 7), rows, width))
    black.append(Objects.king(Black, (3, 7), rows, width))
    return white, black


def main():
    width = 480
    rows = 8
    size = width // rows
    win = pygame.display.set_mode((width, width))
    peices = createList(width, rows)
    white = peices[0]
    black = peices[1]
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(60)
        clock.tick(10)
        redrawWindow(white, black, win, width)
        turn(white, black, size)


if __name__ == '__main__':
    main()
