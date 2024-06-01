# coding: utf-8

from datasPack.jsonDatas import JsonDatas

class DatasBridge(JsonDatas):
    def __init__(self):
        super().__init__()

    """
    Load and Save Grid file
    """
    def loadGrid(self, fileName):
        return self.convertGrid(self.loadJson(fileName), False)

    def writeGrid(self, fileName, datas):
        self.writeJson(fileName, self.convertGrid(datas))

    def saveGrid(self, datas):
        return self.saveJson(self.convertGrid(datas))

    # Convertion grid<=>json
    def convertGrid(self, grid, toJson = True):
        gridBackup = {}

        for x in grid:
            coords = ":".join(map(str, x)) if toJson == True else tuple(map(int, x.split(":")))
            gridBackup[coords] = grid[x]

        return gridBackup