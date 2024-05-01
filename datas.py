# coding: utf-8

import os
import json
from tkinter.filedialog import asksaveasfile

class Datas():
    def __init__(self):
        self.setDefault()

    def findDatas(self, fileName):
        f = open(fileName, "r")
        datas = json.load(f)
        f.close()
        return datas
    
    def datasRead(self, name):
        return self.findDatas(self.directory + name + self.extension)
    
    def setDefault(self):
        self.directory = "jsons/"
        self.extension = ".json"

    def writeDatas(self, datas):
        f = asksaveasfile(mode='w', defaultextension=".json")
        if f != None:
            f.write(json.dumps(datas))
            f.close()