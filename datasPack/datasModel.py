# coding: utf-8

class DatasModel():
    def __init__(self):
        self._fileType = [('Text File', '*.txt'), ('All File','*.*')]
        self._directory = ""
        self._extension = ".txt"

    @property
    def fileType(self):
        return self._fileType

    @fileType.setter
    def fileType(self, fileType):
        self._fileType = fileType

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, directory):
        self._directory = directory

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, extension):
        self._extension = extension