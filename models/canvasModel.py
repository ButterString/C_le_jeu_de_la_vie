# coding: utf-8

from tkinter import Canvas

class CanvasModel():
    def __init__(self, mainWindow):
        # Couleur des cellules vivante
        self._alive = 'white'
        # Couleur des cellules mortes
        self._dead = 'black'
        # Dimensions
        self.setDimensions(900, 900)

        # Déclaration du canvas
        self._canvas = Canvas(mainWindow, width=self.sizeW, height=self.sizeH, bg='black')
        self._canvas.pack()

    # Dimensions du canvas
    def setDimensions(self, w, h):
        self._sizeW = w
        self._sizeH = h

    @property
    def alive(self):
        return self._alive

    @property
    def dead(self):
        return self._dead

    @property
    def canvas(self):
        return self._canvas

    @property
    def sizeW(self):
        return self._sizeW

    @property
    def sizeH(self):
        return self._sizeH

    @alive.setter
    def alive(self, statut):
        self._alive = statut

    @dead.setter
    def dead(self, statut):
        self._dead = statut

    @canvas.setter
    def canvas(self, canvas):
        self._canvas = canvas

    @sizeW.setter
    def sizeW(self, size):
        self._sizeW = size

    @sizeW.setter
    def sizeH(self, size):
        self._sizeH = size