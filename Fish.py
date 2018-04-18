def CreateFishOrNot(fishneighbours):
    return fishneighbours == 3

def ShouldFishDie(fishneighbours):
        # должна ли рыба умереть или продолжить жить
        if (fishneighbours > 1 and fishneighbours < 4):
            return False
        else:
            return True

#**********************************************CELL*******************************************************#
class Cell:
    def is_alive(self):
        return False

    def Graphic_code(self):
        return ' '
#**********************************************ANIMAL*******************************************************#
class Animal(Cell):
    def is_alive(self):
        return True

    def Graphic_code(self):
        return '1'

    def should_die(neighbors):
        return not (self.MIN_NEIGHBORS < neighbors < self.MAX_NEIGHBORS)
#**********************************************Non_alive*******************************************************#
class Non_alive(Cell):
    def is_alive(self):
        return False

    def Graphic_code(self):
        return '-1'
#***********************************************FISH*******************************************************#
class Fish(Animal):
    MIN_NEIGHBORS = 1
    MAX_NEIGHBORS = 4
    WHEN_CREATE = 3

    def ShouldFishDie(fishneighbours):
        # должна ли рыба умереть или продолжить жить
        if (fishneighbours  > MIN_NEIGHBORS and fishneighbours  < MAX_NEIGHBORS ):
            return False
        else:
            return True

    def CreateFishOrNot(fishneighbours):
        # должна ли появиться рыба
        return fishneighbours == WHEN_CREATE

    def Graphic_code(self):
        return 'F'
#**********************************************SHRIMP*******************************************************#
#obj = Fish()
#if type(obj) == Fish:
class Shrimp(Animal):
    MIN_NEIGHBORS = 1
    MAX_NEIGHBORS = 4
    WHEN_CREATE = 3

    def ShouldSrimpDie(shrimpneighbours):
        if (shrimpneighbours  > MIN_NEIGHBORS and shrimpneighbours < MAX_NEIGHBORS):
            return False
        else:
            return True

    def CreateFishOrNot(shrimpneighbours):
        return shrimpneighbours == WHEN_CREATE

    def Graphic_code(self):
        return 'S'

#**********************************************ROCK*******************************************************#
class Rock(Non_alive):

    def is_alive(self):
        return False

    def Graphic_code(self):
        return '-1'

    def Graphic_code(self):
        return 'R'

#**********************************************************************************************************#