class Cell:
    def IsEmpty(self):
        return True

    def IsAlive(self):
        return False

    def ShouldDie(self):
        return self

    def create(self, type ):
        if type == 1:
            return Fish()
        if type == 2:
            return Shrimp()
        if type == -1:
            return Rock()
        return self

    def ShouldBeBorn(self, neigh):
        c1 = Fish()
        c2 = Shrimp()
        if neigh[1] == c1.NUM_TO_CREATE:
            return c1
        if neigh[2] == c2.NUM_TO_CREATE:
            return c2
        return self

    def PrintMe(self):
       return "~ "

    def NumOfType(self):# every non empty cell has type to calculate neigh easier
        pass

class Fish(Cell):
    MIN_NEIGH = 2
    MAX_NEIGH = 3
    NUM_TO_CREATE = 3

    def IsEmpty(self):
        return False

    def IsAlive(self):
        return True

    def PrintMe(self):
        return "F "

    def ShouldDie(self, neigh):
        if (neigh > 1 and neigh < 4):
            return self
        else:
            return Cell()

    def ShouldBeBorn(self):
        pass

    def NumOfType(self):
        return 1

class Shrimp(Cell):
    MIN_NEIGH = 2
    MAX_NEIGH = 3
    NUM_TO_CREATE = 3

    def IsEmpty(self):
        return False

    def IsAlive(self):
        return True

    def PrintMe(self):
        return "S "

    def ShouldDie(self, neigh):
        if (neigh > 1 and neigh < 4):
            return self
        else:
            return Cell()

    def ShouldBeBorn(self):
        pass

    def NumOfType(self):
        return 2


class Rock(Cell):

    def IsEmpty(self):
        return False

    def PrintMe(self):
        return "R "

    def ShouldDie(self, neigh):
        return self


    def ShouldBeBorn(self):
        pass

    def NumOfType(self):
        return -1
#**********************************************