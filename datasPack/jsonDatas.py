# coding: utf-8

import json

from datasPack.datas import Datas

class JsonDatas(Datas):
    def __init__(self):
        super().__init__()

        self._directory = "jsons/"
        self._extension = ".json"
        self._fileType = [('JSON files','*.json')]

    def jsonRead(self, name):
        return json.loads(self.datasRead(name))

    def loadJson(self, fileName):
        return json.loads(self.loadDatas(fileName))

    def findJson(self):
        return self.findDatas()

    def saveJson(self, datas):        
        return self.saveDatas(json.dumps(datas))

    def writeJson(self, fileName, datas):
        self.writeDatas(fileName, json.dumps(datas))
