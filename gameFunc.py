import time

import Fish
import Shrimp

def PrintField(field):
    for i in range(len(field)):
        result = [str(item) for item in field[i]]
        for j in range(len(result)):
            if result[j] =='-1':
                result[j]='R'
            if result[j] =='1':
                result[j]='F'
            if result[j] =='2':
                result[j]='S'
        print(*result)
    print()


def CreateField(n):
    field = [0] * n
    for i in range(n):
        field[i] = [0] * n
    return field


def isNotThere(x, y, allAlive):
    for i in range(len(allAlive[0])):
        if (allAlive[0][i] == x and allAlive[1][i] == y):
            return False
    return True

def AddToFieldFromFile(allAlive, values=[-1, 1, 2]):
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
            field[int(result[j])][int(result[j + 1])] = values[i]
            if (values[i] > 0):
                allAlive[0].append(int(result[j]) % n);
                allAlive[1].append(int(result[j + 1]) % n);
            j = j + 2
    return field

def AddToField(allAlive, values=[-1, 1, 2]):  # number of types pf data : rock, fish, shrimp
    n = int(input())
    field = []
    field = CreateField(n)
    for i in range(len(values)):
        newdata = input().split()
        j = 0
        while j < len(newdata):
            field[int(newdata[j])][int(newdata[j + 1])] = values[i]
            if (values[i] > 0):
                allAlive[0].append(int(newdata[j]) % n);
                allAlive[1].append(int(newdata[j + 1]) % n);
            j = j + 2
    return field

def CalculateNeighbours(field, x, y, values=[-1, 1, 2]):
    dim = len(field[0])
    neighbours = [0] * len(values)
    x -= 1
    y -= 1
    for i in range(3):
        for j in range(3):
            if field[(x + i) % dim][(y + j) % dim] != 0:
                #                print(values.index(field[(x + i) % dim][(y + j) % dim]))
                #               newvalue = values.index(field[(x + i) % dim][(y + j) % dim])
                neighbours[values.index(field[(x + i) % dim][(y + j) % dim])] += 1
    if field[(x + 1) % dim][(y + 1) % dim] != 0:
        neighbours[values.index(field[(x + 1) % dim][(y + 1) % dim])] = neighbours[values.index(
            field[(x + 1) % dim][(y + 1) % dim])] - 1
    # print(field)
    return neighbours


def NextStep(field, allAlive):
    dim = len(field[0])
    # newfield = CreateField(dim)
    newfield = [0] * dim
    for i in range(dim):
        newfield[i] = [0] * dim
    for m in range(dim):
        for l in range(dim):
            newfield[m][l] = field[m][l]
    # newfield = field
    # print(newfield)
    # all alive cells and heir neigh are being put into list aliveNow
    aliveNow = [[], []]
    for i in range(len(allAlive[0])):
        x = (allAlive[0][i] - 1) % dim
        y = (allAlive[1][i] - 1) % dim
        for j in range(3):
            for k in range(3):
                if isNotThere((x + j) % dim, (y + k) % dim, aliveNow):
                    aliveNow[0].append((x + j) % dim)
                    aliveNow[1].append((y + k) % dim)
    # print(aliveNow)
    while (len(allAlive[1]) > 0):
        allAlive[0].pop()
        allAlive[1].pop()
    # print(allAlive)
    for i in range(len(aliveNow[0])):
        neigh = CalculateNeighbours(field, aliveNow[0][i], aliveNow[1][i])
        # print(neigh)
        if (field[aliveNow[0][i]][aliveNow[1][i]] == 0):
            if Shrimp.CreateShrimpOrNot(neigh[2]):
                #                print("you ll appear S")
                newfield[aliveNow[0][i]][aliveNow[1][i]] = 2
                allAlive[0].append(int(aliveNow[0][i]))
                allAlive[1].append(int(aliveNow[1][i]))
            if Fish.CreateFishOrNot(neigh[1]):
                #                print("you ll appear F")
                newfield[aliveNow[0][i]][aliveNow[1][i]] = 1
                # var1 = aliveNow[0][i]
                allAlive[0].append(int(aliveNow[0][i]))
                allAlive[1].append(int(aliveNow[1][i]))
        if (field[aliveNow[0][i]][aliveNow[1][i]] > 0):
            if field[aliveNow[0][i]][aliveNow[1][i]] == 1:
                if Fish.ShouldFishDie(neigh[1]):
                    #                   print("you ll die")
                    newfield[aliveNow[0][i] % dim][aliveNow[1][i] % dim] = 0
                else:
                    #                   print("you ll survive")
                    newfield[aliveNow[0][i] % dim][aliveNow[1][i] % dim] = 1
                    allAlive[0].append(int(aliveNow[0][i]))
                    allAlive[1].append(int(aliveNow[1][i]))
            if field[aliveNow[0][i]][aliveNow[1][i]] == 2:
                if Shrimp.ShouldSrimpDie(neigh[2]):
                    #                    print("you ll die")
                    newfield[aliveNow[0][i] % dim][aliveNow[1][i] % dim] = 0
                else:
                    #                  print("you ll survive")
                    newfield[aliveNow[0][i] % dim][aliveNow[1][i] % dim] = 2
                    allAlive[0].append(int(aliveNow[0][i]))
                    allAlive[1].append(int(aliveNow[1][i]))
    # PrintField(newfield)
    # print(allAlive[0])
    # print(allAlive[1])
    #time.sleep(3)
    return newfield


def GameOfLife():
    field = []
    allAlive = [[], []]
    print("Do you want to read from file(F) or console(C)")
    typeofInput = input()
    if (typeofInput == 'F'):
        field = AddToFieldFromFile(allAlive)
    else:
        field = AddToField(allAlive)

    PrintField(field)
    time.sleep(4)
    i = 1
    while (True):
        field = NextStep(field, allAlive)
        print('Number of generation:', i,'\n')
        i+=1
        #time.sleep(4)
#GameOfLife()
