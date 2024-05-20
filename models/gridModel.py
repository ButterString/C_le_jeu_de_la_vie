# coding: utf-8

class GridModel():
    def __init__(self):
        # Dimensions par défaut
        self._sizeL = 30
        self._sizeC = 30
        # valeur des cellules vivantes
        self._alive = 1
        # valeur des cellules mortes
        self._dead = 0
        # Tableau des états des cellules (pour la génération aléatoire)
        self._states = [self._alive, self._dead]
        # Déclaration du rayon d'influence
        self._influence = 3
        # Initialisation de la grille
        self._grid = []

    @property
    def sizeL(self):
        return self._sizeL

    @property
    def sizeC(self):
        return self._sizeC

    @property
    def alive(self):
        return self._alive

    @property
    def dead(self):
        return self._dead

    @property
    def states(self):
        return self._states

    @property
    def influence(self):
        return self._influence

    @property
    def grid(self):
        return self._grid

    @sizeL.setter
    def sizeL(self, size):
        self._sizeL = size

    @sizeC.setter
    def sizeC(self, size):
        self._sizeC = size

    @alive.setter
    def alive(self, value):
        self._alive = value

    @dead.setter
    def dead(self, value):
        self._dead = value

    @states.setter
    def states(self, states):
        self._states = states

    @influence.setter
    def influence(self, value):
        self._influence = value

    @grid.setter
    def grid(self, grid):
        self._grid = grid