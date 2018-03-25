def ShouldFishDie(fishneighbours):
#должна ли рыба умереть или продолжить жить
    if(fishneighbours == 3 or fishneighbours == 2 ):
        return False
    else: return True

def CreateFishOrNot( fishneighbours):
#должна ли появиться рыба
    if(fishneighbours == 3):
        return True
    else: return False