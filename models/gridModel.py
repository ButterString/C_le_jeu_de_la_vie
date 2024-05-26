# coding: utf-8

class GridModel():
    def __init__(self, config):
        # Dimensions par défaut
        self._steps = tuple(config["steps"])
        # valeur des cellules vivantes
        self._alive = config["alive"]
        # valeur des cellules mortes
        self._dead = config["dead"]
        # Tableau des états des cellules (pour la génération aléatoire)
        self._states = (self._alive, self._dead)
        # Déclaration du rayon d'influence
        self._influence = config["influence"]
        # Initialisation de la grille
        self._grid = {}

    @property
    def steps(self):
        return self._steps

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

    @steps.setter
    def steps(self, x, y):
        self._steps = (x, y)

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