# coding: utf-8

import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

class JsonDatas():
    def __init__(self):
        self.setDefault()
    
    def setDefault(self):
        self._directory = "jsons/"
        self.extension = ".json"
    
    def jsonRead(self, name):
        return self.findJson(self._directory + name + self.extension)

    def findJson(self, fileName):
        if fileName != '':
            f = open(fileName, "r")
            datas = json.load(f)
            f.close()
            return datas
    
    def loadJson(self):
        f = askopenfilename(
            initialdir = self._directory,
            title="sélectionner votre grille",
            filetypes=[('JSON files','.json'), ("all files", "*.*")]
        )
        return f if f != "" else False

    def saveJson(self, datas):
        f = asksaveasfile(initialdir = self._directory, mode='w', defaultextension=".json")
        filename = f.name if f != None else False
        if filename != False:
            f.write(json.dumps(datas))
            f.close()
        return filename

    def writeJson(self, fileName, datas):
        f = open(fileName, "w")
        f.write(json.dumps(datas))
        f.close()

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, directory):
        self._directory = directory
