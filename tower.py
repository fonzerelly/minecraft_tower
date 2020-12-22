def createTowerAt(position):
    # return "Hallo Tower"
    centerOfTower =  [
        (position.getX() - 1, position.getY(), position.getZ() + 4)
    ]
    wallToTheRight = [
        (position.getX() + 1, position.getY(), position.getZ() + 2),
        (position.getX() + 1, position.getY(), position.getZ() + 3),
        (position.getX() + 1, position.getY(), position.getZ() + 4),
        (position.getX() + 1, position.getY(), position.getZ() + 5),
        (position.getX() + 1, position.getY(), position.getZ() + 6)
    ]
    wallToTheLeft = [
        (position.getX() - 3, position.getY(), position.getZ() + 2),
        (position.getX() - 3, position.getY(), position.getZ() + 3),
        (position.getX() - 3, position.getY(), position.getZ() + 4),
        (position.getX() - 3, position.getY(), position.getZ() + 5),
        (position.getX() - 3, position.getY(), position.getZ() + 6)
    ]
    wallToTheLeft = [
        (position.getX() - 3, position.getY(), position.getZ() + 2),
        (position.getX() - 3, position.getY(), position.getZ() + 3),
        (position.getX() - 3, position.getY(), position.getZ() + 4),
        (position.getX() - 3, position.getY(), position.getZ() + 5),
        (position.getX() - 3, position.getY(), position.getZ() + 6)
    ]
    wallAtBack = [
        (position.getX() - 2, position.getY(), position.getZ() + 6),
        (position.getX() - 1, position.getY(), position.getZ() + 6),
        (position.getX() - 0, position.getY(), position.getZ() + 6),
    ]
    wallAtFront = [
        (position.getX() - 2, position.getY(), position.getZ() + 2),
        (position.getX() - 1, position.getY(), position.getZ() + 2),
        (position.getX() - 0, position.getY(), position.getZ() + 2),
    ]
    return wallAtBack + wallToTheLeft + centerOfTower + wallToTheRight + wallAtFront
    # return [(1, 2, 3)]