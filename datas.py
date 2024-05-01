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