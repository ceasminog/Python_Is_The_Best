import time
import  Creatures
from Creatures import *
#**********************************************
# SomeClassName
# some_variable_name
# SOME_CONSTANT_NAME

def GetField(field):
    p = len(field)
    graphic_field = [''] * p
    for i in range(p):
        result = []
        for j in range(len(field)):
            result.append(field[i][j].PrintMe())
        a = ''.join(result)
        graphic_field[i] = a
    return graphic_field

def CreateField(n):
    c = Cell()
    field = [c] * n
    for i in range(n):
        field[i] = [c] * n
    return field


def isNotThere(x, y, all_alive):
    for i in range(len(all_alive[0])):
        if (all_alive[0][i] == x and all_alive[1][i] == y):
            return False
    return True


def AddToFieldFromFile(all_alive, values=[-1, 1, 2]):
    f = open('textFile.txt', 'r')
    n = int(f.readline())
    field = []
    field = CreateField(n)
    for i in range(len(values)):
        a = f.readline().rstrip().split(' ')
        if (a != ['']):
            result = [int(item) for item in a]
        else:
            result = []
        j = 0
        while j < len(result):
            x = int(result[j])
            y = int(result[j + 1])
            new_c = Cell()
            field[x][y] = new_c.create(values[i])
            if (values[i] > 0):
                all_alive[0].append(int(result[j]) % n);
                all_alive[1].append(int(result[j + 1]) % n);
            j = j + 2
    return field

def CalculateNeighbours(field, x, y, values=[-1, 1, 2]):
    dim = len(field[0])
    neighbours = [0] * len(values)
    x -= 1
    y -= 1
    for i in range(3):
        for j in range(3):
            if not field[(x + i) % dim][(y + j) % dim].IsEmpty():
                k = values.index(field[(x + i) % dim][(y + j) % dim].NumOfType())
                neighbours[k] += 1
    x+=1
    y+=1
    if not field[(x) % dim][(y) % dim].IsEmpty():
        neighbours[field[(x) % dim][(y) % dim].NumOfType()] -= 1
    return neighbours


def NextStep(field, all_alive):
    dim = len(field[0])
    c = Cell()
    newfield = [c] * dim
    for i in range(dim):
        newfield[i] = [c] * dim
    for m in range(dim):
        for l in range(dim):
            newfield[m][l] = field[m][l]
    # all alive cells and heir neigh are being put into list alive_now
    alive_now = [[], []]
    for i in range(len(all_alive[0])):
        x = (all_alive[0][i] - 1) % dim
        y = (all_alive[1][i] - 1) % dim
        for j in range(3):
            for k in range(3):
                if isNotThere((x + j) % dim, (y + k) % dim, alive_now):
                    alive_now[0].append((x + j) % dim)
                    alive_now[1].append((y + k) % dim)
    while (len(all_alive[1]) > 0):
        all_alive[0].pop()
        all_alive[1].pop()
    for i in range(len(alive_now[0])):
        neigh = CalculateNeighbours(field, alive_now[0][i], alive_now[1][i])
        x1 = int(alive_now[0][i])
        y1 = int(alive_now[1][i])
        if (field[x1][y1].IsEmpty()):
            newfield[x1][y1].ShouldBeBorn(neigh)
            if field[x1][y1].IsAlive():
                all_alive[0].append(x1)
                all_alive[1].append(y1)
        if (field[x1][y1].IsAlive()):
            newfield[x1][y1] = field[x1][y1].ShouldDie(neigh[field[x1][y1].NumOfType()])
            if field[x1][y1].IsAlive:
                all_alive[0].append(x1)
                all_alive[1].append(y1)
    return newfield
