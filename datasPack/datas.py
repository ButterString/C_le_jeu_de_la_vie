# coding: utf-8

from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

from datasPack.datasModel import DatasModel

class Datas(DatasModel):
    def __init__(self):
        super().__init__()

    def addFileType(self, fileType):
        self._fileType.append(fileType)
    
    def datasRead(self, name):
        return self.loadDatas(self._directory + name + self._extension)

    def loadDatas(self, fileName):
        f = open(fileName, "r")
        datas = f.read()
        f.close()

        return datas
    
    def findDatas(self):
        f = askopenfilename(
            initialdir = self._directory,
            title="select files",
            filetypes=self.fileType
        )

        return f if f != "" else False

    def saveDatas(self, datas):
        f = asksaveasfile(
            initialdir = self._directory,
            mode='w',
            defaultextension=self.extension,
            filetypes=self.fileType
        )
        fileName = f.name if f != None else False
        f.close()

        return fileName

    def writeDatas(self, fileName, datas):
        f = open(fileName, "w")
        f.write(datas)
        f.close()