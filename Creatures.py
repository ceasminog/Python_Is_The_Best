class Cell:
    def is_empty(self):
        return True

    def is_alive(self):
        return False

    def should_die(self):
        return self

    def create(self, type ):
        if type == 1:
            return Fish()
        if type == 2:
            return Shrimp()
        if type == -1:
            return Rock()
        return self

    def should_be_born(self, neigh):
        c1 = Fish()
        c2 = Shrimp()
        if neigh[1] == c1.NUM_TO_CREATE:
            return c1
        if neigh[2] == c2.NUM_TO_CREATE:
            return c2
        return self

    def __str__(self):
       return "~ "

    def num_of_type(self):# every non empty cell has type to calculate neigh easier
        pass

class Fish(Cell):
    MIN_NEIGH = 2
    MAX_NEIGH = 3
    NUM_TO_CREATE = 3

    def is_empty(self):
        return False

    def is_alive(self):
        return True

    def __str__(self):
        return "F "

    def should_die(self, neigh):
        if (neigh > 1 and neigh < 4):
            return self
        else:
            return Cell()

    def should_be_born(self):
        pass

    def num_of_type(self):
        return 1

class Shrimp(Cell):
    MIN_NEIGH = 2
    MAX_NEIGH = 3
    NUM_TO_CREATE = 3

    def is_empty(self):
        return False

    def is_alive(self):
        return True

    def __str__(self):
        return "S "

    def should_die(self, neigh):
        if (neigh > 1 and neigh < 4):
            return self
        else:
            return Cell()

    def should_be_born(self):
        pass

    def num_of_type(self):
        return 2


class Rock(Cell):

    def is_empty(self):
        return False

    def __str__(self):
        return "R "

    def should_die(self, neigh):
        return self


    def should_be_born(self):
        pass

    def num_of_type(self):
        return -1
#**********************************************