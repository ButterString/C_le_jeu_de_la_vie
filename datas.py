# coding: utf-8

import os
import json

class Datas():
    def __init__(self):
        self.setDefault()

    def findDatas(self, fileName):
        f = open(fileName, "r")
        return json.load(f)
    
    def datasRead(self, name):
        return self.findDatas(self.directory + name + self.extension)
    
    def setDefault(self):
        self.directory = "jsons/"
        self.extension = ".json"
    
    def getDirGrids(self):
        return "jsons/grids"
    
    def getGrids(self):
        return self.getCustomGrids(self.getDirGrids())
    
    def getCustomGrids(self, dirGrids):
        grids = []
        files = os.listdir(dirGrids)

        for f in files:
            grids.append(dirGrids + "/" + f)
        
        return grids