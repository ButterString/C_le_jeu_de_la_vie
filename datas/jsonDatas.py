# coding: utf-8

import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

class JsonDatas():
    def __init__(self):
        self.setDefault()
    
    def setDefault(self):
        self.directory = "jsons/"
        self.extension = ".json"
    
    def jsonRead(self, name):
        return self.findJson(self.directory + name + self.extension)

    def findJson(self, fileName):
        if fileName != '':
            f = open(fileName, "r")
            datas = json.load(f)
            f.close()
            return datas
    
    def loadJson(self):
        return askopenfilename(title="sélectionner votre grille",filetypes=[('JSON files','.json')])

    def writeJson(self, datas):
        f = asksaveasfile(mode='w', defaultextension=".json")
        if f != None:
            f.write(json.dumps(datas))
            f.close()