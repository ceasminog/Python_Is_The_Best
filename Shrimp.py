def CreateShrimpOrNot(shrimpneighbours):
    return shrimpneighbours == 3

def ShouldSrimpDie(shrimpneig):
    if (shrimpneig > 1 and shrimpneig < 4):
        return False
    else:
        return True