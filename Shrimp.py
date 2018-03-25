def ShouldSrimpDie(shrimpneighbours):
#должна ли креветка умереть или продолжить жить
    if(shrimpneighbours == 3 or shrimpneighbours == 2 ):
        return False
    else: return True

def CreateShrimpOrNot(shrimpneighbours):
#должна ли креветка появиться
    if(shrimpneighbours == 3):
        return True
    else: return False