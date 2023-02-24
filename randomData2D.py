

class RandomTerrain:

    gridDict = {}

    def __init__(self):
        pass

    def generateGrid(self, xRadius, yRadius):
        for x in range(-xRadius, xRadius + 1):
            for y in range(-yRadius, yRadius + 1):
                gridDict[(x,y)] = new TerrainSquare()
    
