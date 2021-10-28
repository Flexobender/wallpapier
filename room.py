import math


class Room:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.wd = []

    def addWD(self, WD):
        self.wd.append(WD)

    def roomSquare(self):
        square = 2 * self.z * (self.x + self.y)
        return square

    def workSurface(self):
        workSurface = self.roomSquare()
        for i in self.wd:
            workSurface -= i.w * i.h
        return workSurface


class WinDoor:
    def __init__(self, w, h):
        self.w = w
        self.h = h


def rollsNeed(room, w, l):
    sq = w * l
    qt = math.ceil(room.workSurface() / sq)
    return qt
