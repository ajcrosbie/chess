import pygame


class peice():
    def __init__(self, colour, pos, rows, w):
        self.colour = colour
        self.pos = pos
        self.rows = rows
        self.w = w
        self.type = 0
        self.size = self.w // self.rows - 2
        self.dis = self.w // self.rows

    def take(self, peice1):
        pass

    def draw(self, win):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        self.size = dis-2
        pygame.draw.rect(win, self.colour,
                         (i*dis+1, j*dis+1, dis-2, dis-2))
        x = (i*dis + dis//2, j*dis + dis//2)

        if self.type == 'king':
            pygame.draw.circle(
                win, (0, 255, 0), x, dis//4)
        if self.type == 'queen':
            pygame.draw.circle(
                win, (255, 0, 0), x, dis//4)
        if self.type == 'knight':
            pygame.draw.circle(
                win, (100, 100, 0), x, dis//4)
        if self.type == 'bishop':
            pygame.draw.circle(
                win, (0, 50, 50), x, dis//4)
        if self.type == 'rook':
            pygame.draw.circle(
                win, (200, 0, 200), x, dis//4)

    def check(self, location, immovable, killable):
        for g in range(len(immovable)):
            if immovable[g][0] == location[0] + self.pos[0]:
                if immovable[g][1] == location[1] + self.pos[1]:
                    print(immovable[g][0], immovable[g][1])
                    t = False
                    print(immovable[g][0], immovable[g][1])
                    break
                else:
                    t = True
            else:
                t = True
        return t

    def move(self, Alies, enimies, po):
        t = True
        immovable = []
        killable = []
        for i in Alies:
            immovable.append(i.pos)
        for i in enimies:
            killable.append(i.pos)
        x = len(self.allowable)
        if self.type == 'pawn':
            if self.pos[1] == 1 and self.colour == (255, 255, 255):
                self.allowable.append(-2, 0)
                tlo = 1
            if self.pos[1] == 6 and self.colour == (255, 255, 255):
                self.allowable.append(-2, 0)
                tlo = 1
        t = False
        u = True
        for i in range(x):
            if self.pos[0] + self.allowable[i][0] == po[0]:
                if self.pos[1] + self.allowable[i][1] == po[1]:
                    for g in range(len(immovable)):
                        if immovable[g][0] == po[0]:
                            if immovable[g][1] == po[1]:
                                t = False
                                break
                            else:
                                t = True
                        else:
                            t = True

                    if self.type == 'knight' or self.type == 'king':
                        u = True
                    else:
                        g = self.allowable[i][0]
                        h = self.allowable[i][1]
                        while g != 0 and h != 0:
                            if g > 0:
                                g = g - 1
                            if g < 0:
                                g = g + 1
                            if h > 0:
                                h = h - 1
                            if h < 0:
                                h + 1
                            if g != 0 and h != 0:
                                print('p')
                                u = self.check((g, h), immovable, killable)
                                print(u)
                            if not u:
                                break
        print(t, u)
        if t and u:
            self.pos = po

        if self.type == 'pawn' and tlo == 1:
            try:
                self.allowable.remove((-2, 0))
            except:
                pass
            try:
                self.allowable.remove((2, 0))
            except:
                pass


class king(peice):
    def __init__(self, colour, pos, rows, w):
        super().__init__(colour, pos, rows, w)
        self.type = 'king'
        self.allowable = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    def death(self):
        pass


class queen(peice):
    def __init__(self, colour, pos, rows, w):
        super().__init__(colour, pos, rows, w)
        self.type = 'queen'
        self.allowable = []
        self.allowableT = []
        for i in range(self.rows*2):
            self.allowable.append((0, i-self.rows))
            self.allowable.append((i-self.rows, 0))
        for i in range(rows):
            self.allowable.append((i, i))
            self.allowable.append((i, -i))
            self.allowable.append((-i, i))
            self.allowable.append((-i, -i))


class knight(peice):
    def __init__(self, colour, pos, rows, w):
        super().__init__(colour, pos, rows, w)
        self.type = 'knight'
        self.allowable = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                          (-1, 2), (-1, -2), (1, -2), (1, 2)]


class bishop(peice):
    def __init__(self, colour, pos, rows, w):
        super().__init__(colour, pos, rows, w)
        self.type = 'bishop'
        self.allowable = []
        for i in range(rows):
            self.allowable.append((i, i))
            self.allowable.append((i, -i))
            self.allowable.append((-i, i))
            self.allowable.append((-i, -i))


class rook(peice):
    def __init__(self, colour, pos, rows, w):
        super().__init__(colour, pos, rows, w)
        self.type = 'rook'
        self.allowable = []
        for i in range(self.rows*2):
            self.allowable.append((0, i-self.rows))
            self.allowable.append((i-self.rows, 0))


class pawn(peice):
    def __init__(self, colour, pos, rows, w):
        super().__init__(colour, pos, rows, w)
        self.type = 'pawn'
        self.opos = pos
        self.allowable = []

    def promote(self):
        pass
