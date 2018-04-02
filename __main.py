import time

# **********************************************CELL*******************************************************#
class Cell:
    def __init__(self):
        pass

    def is_alive(self):
        return False

    def Graphic_code(self):
        return ' '


# **********************************************ANIMAL*******************************************************#
class Animal(Cell):

    def __init__(self):
        pass

    def is_alive(self):
        return True

    def Graphic_code(self):
        return '1'

    def should_die(neighbors):
        return not (self.MIN_NEIGHBORS < neighbors < self.MAX_NEIGHBORS)


# **********************************************Non_alive*******************************************************#
class Non_alive(Cell):

    def __init__(self):
        pass

    def is_alive(self):
        return False

    def Graphic_code(self):
        return '-1'


# **********************************************EMPTY*CELL******************************************************#

class Empty_cell:
    def __init__(self):
        pass

    def is_alive(self):
        return False

    WHEN_CREATE_SHRIMP = 3

    def create_shrimp_or_not(self, shrimpneighbours):
        return shrimpneighbours == 3

    WHEN_CREATE_FISH = 3

    def create_fish_or_not(self, fishneighbours):
        # должна ли появиться рыба
        return fishneighbours == 3

# ***************************************FISH***********************************************************#


class Fish(Animal):
    def __init__(self):
        pass

    MIN_NEIGHBORS = 1
    MAX_NEIGHBORS = 4

    def ShouldFishDie(self, fishneighbours):
        # должна ли рыба умереть или продолжить жить
        if (fishneighbours > 1 and fishneighbours < 4):
            return False
        else:
            return True

    def Graphic_code(self):
        return 'F'
# **********************************************SHRIMP*******************************************************#


class Shrimp(Animal):
    def __init__(self):
        pass

    MIN_NEIGHBORS = 1
    MAX_NEIGHBORS = 4

    def ShouldSrimpDie(self, shrimpneig):
        if (shrimpneig > 1 and shrimpneig < 4):
            return False
        else:
            return True

    def Graphic_code(self):
        return 'S'

# **********************************************ROCK*******************************************************#


class Rock(Non_alive):
    def __init__(self):
        pass

    def is_alive(self):
        return False

    def Graphic_code(self):
        return 'R'

# **********************************************************************************************************#


def print_field(field):
    for i in range(len(field)):
        result = [str(item) for item in field[i]]
        for j in range(len(result)):
            if result[j] =='-1':
                result[j]='R'
            if result[j] =='1':
                result[j]='F'
            if result[j] =='2':
                result[j]='S'
            if result[j] =='0':
                result[j]='~'
        print(*result)
    print()


def create_field(n):
    field = [0] * n
    for i in range(n):
        field[i] = [0] * n
    return field


def is_not_there(x, y, all_alive):
    for i in range(len(all_alive[0])):
        if (all_alive[0][i] == x and all_alive[1][i] == y):
            return False
    return True


def Add_from_file(all_alive, values=[-1, 1, 2]):
    f = open('readFrom.txt', 'r')
    n = int(f.readline())
    field = []
    field = create_field(n)
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
                all_alive[0].append(int(result[j]) % n);
                all_alive[1].append(int(result[j + 1]) % n);
            j = j + 2
    return field


def Add_to_field(all_alive, values=[-1, 1, 2]):  # number of types pf data : rock, fish, shrimp
    n = int(input())
    field = []
    field = create_field(n)
    for i in range(len(values)):
        newdata = input().split()
        j = 0
        while j < len(newdata):
            field[int(newdata[j])][int(newdata[j + 1])] = values[i]
            if (values[i] > 0):
                all_alive[0].append(int(newdata[j]) % n);
                all_alive[1].append(int(newdata[j + 1]) % n);
            j = j + 2
    return field

def calculate_neighbours(field, x, y, values=[-1, 1, 2]):
    dim = len(field[0])
    neighbours = [0] * len(values)
    x -= 1
    y -= 1
    for i in range(3):
        for j in range(3):
            if field[(x + i) % dim][(y + j) % dim] != 0:
                neighbours[values.index(field[(x + i) % dim][(y + j) % dim])] += 1
    if field[(x + 1) % dim][(y + 1) % dim] != 0:
        neighbours[values.index(field[(x + 1) % dim][(y + 1) % dim])] = neighbours[values.index(
            field[(x + 1) % dim][(y + 1) % dim])] - 1
    return neighbours


def Next_step(field, all_alive):
    dim = len(field[0])
    newfield = [0] * dim
    for i in range(dim):
        newfield[i] = [0] * dim
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
                if is_not_there((x + j) % dim, (y + k) % dim, alive_now):
                    alive_now[0].append((x + j) % dim)
                    alive_now[1].append((y + k) % dim)
    while (len(all_alive[1]) > 0):
        all_alive[0].pop()
        all_alive[1].pop()
    for i in range(len(alive_now[0])):
        neigh = calculate_neighbours(field, alive_now[0][i], alive_now[1][i])
        if (field[alive_now[0][i]][alive_now[1][i]] == 0):
            obj1 = Empty_cell()
            if obj1.create_shrimp_or_not(neigh[2]):
                newfield[alive_now[0][i]][alive_now[1][i]] = 2
                all_alive[0].append(int(alive_now[0][i]))
                all_alive[1].append(int(alive_now[1][i]))
            if obj1.create_fish_or_not(neigh[1]):
                newfield[alive_now[0][i]][alive_now[1][i]] = 1
                all_alive[0].append(int(alive_now[0][i]))
                all_alive[1].append(int(alive_now[1][i]))
        if (field[alive_now[0][i]][alive_now[1][i]] > 0):
            if field[alive_now[0][i]][alive_now[1][i]] == 1:
                obj2 = Fish()
                if obj2.ShouldFishDie(neigh[1]):
                    newfield[alive_now[0][i] % dim][alive_now[1][i] % dim] = 0
                else:
                    newfield[alive_now[0][i] % dim][alive_now[1][i] % dim] = 1
                    all_alive[0].append(int(alive_now[0][i]))
                    all_alive[1].append(int(alive_now[1][i]))
            if field[alive_now[0][i]][alive_now[1][i]] == 2:
                obj3 = Shrimp()
                if obj3.ShouldSrimpDie(neigh[2]):
                    newfield[alive_now[0][i] % dim][alive_now[1][i] % dim] = 0
                else:
                    newfield[alive_now[0][i] % dim][alive_now[1][i] % dim] = 2
                    all_alive[0].append(int(alive_now[0][i]))
                    all_alive[1].append(int(alive_now[1][i]))
    print_field(newfield)
    return newfield


def Game_of_life():
    field = []
    all_alive = [[], []]
    print("Do you want to read from file(F) or console(C)")
    typeofInput = input()
    if (typeofInput == 'F'):
        field = Add_from_file(all_alive)
    else:
        field = Add_to_field(all_alive)

    print_field(field)
    print('Number of generation: 0', '\n')
    time.sleep(2)
    i = 1
    while (True):
        field = Next_step(field, all_alive)
        print('Number of generation:', i,'\n')
        i+=1
        time.sleep(2)

Game_of_life()