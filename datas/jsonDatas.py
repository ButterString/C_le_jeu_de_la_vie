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
        f = askopenfilename(title="sélectionner votre grille",filetypes=[('JSON files','.json')])
        return f if f != "" else False

    def saveJson(self, datas):
        f = asksaveasfile(mode='w', defaultextension=".json")
        filename = f.name if f != None else False
        f.write(json.dumps(datas))
        f.close()
        return filename

    def writeJson(self, fileName, datas):
        f = open(fileName, "w")
        f.write(json.dumps(datas))
        f.close()