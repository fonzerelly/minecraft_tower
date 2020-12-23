def createLayerAtWithDoor(position, height):
    centerOfTower =  [
        (position.getX() - 1, position.getY() + height, position.getZ() + 4)
    ]
    wallToTheRight = [
        (position.getX() + 1, position.getY() + height, position.getZ() + 2),
        (position.getX() + 1, position.getY() + height, position.getZ() + 3),
        (position.getX() + 1, position.getY() + height, position.getZ() + 4),
        (position.getX() + 1, position.getY() + height, position.getZ() + 5),
        (position.getX() + 1, position.getY() + height, position.getZ() + 6)
    ]
    wallToTheLeft = [
        (position.getX() - 3, position.getY() + height, position.getZ() + 2),
        (position.getX() - 3, position.getY() + height, position.getZ() + 3),
        (position.getX() - 3, position.getY() + height, position.getZ() + 4),
        (position.getX() - 3, position.getY() + height, position.getZ() + 5),
        (position.getX() - 3, position.getY() + height, position.getZ() + 6)
    ]
    wallAtBack = [
        (position.getX() - 2, position.getY() + height, position.getZ() + 6),
        (position.getX() - 1, position.getY() + height, position.getZ() + 6),
        (position.getX() - 0, position.getY() + height, position.getZ() + 6),
    ]
    wallAtFront = [
        (position.getX() - 2, position.getY() + height, position.getZ() + 2),
        (position.getX() - 1, position.getY() + height, position.getZ() + 2),
        
    ]
    return wallAtBack + wallToTheLeft + centerOfTower + wallToTheRight + wallAtFront

def createLayerAt(position, height):
    return createLayerAtWithDoor(position, height) + [(position.getX() - 0, position.getY() + height, position.getZ() + 2),]

def createStep(position, height):
    steps = [
        [
            (position.getX() +  0, position.getY() + height, position.getZ() + 3), 
            (position.getX() +  0, position.getY() + height, position.getZ() + 4), 
            (position.getX() +  0, position.getY() + height, position.getZ() + 5)
        ],
        [
            (position.getX() +  0, position.getY() + height, position.getZ() + 5),
            (position.getX() + -1, position.getY() + height, position.getZ() + 5),
            (position.getX() + -2, position.getY() + height, position.getZ() + 5)
        ],
        [
            (position.getX() + -2, position.getY() + height, position.getZ() + 5),
            (position.getX() + -2, position.getY() + height, position.getZ() + 4), 
            (position.getX() + -2, position.getY() + height, position.getZ() + 3) 
        ],
        [
            (position.getX() + -2, position.getY() + height, position.getZ() + 3),
            (position.getX() + -1, position.getY() + height, position.getZ() + 3),
            (position.getX() +  0, position.getY() + height, position.getZ() + 3)
        ],
    ]
    return steps[height%len(steps)]

def createTowerAt(position, height):
    result = []
    for i in range(height):
        if (i < 3):
            result += createLayerAtWithDoor(position, i)
        else:
            result += createLayerAt(position, i)
        result += createStep(position, i)
    return result