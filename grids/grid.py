# coding: utf-8

import random
import copy

from models.gridModel import GridModel

class Grid(GridModel):
    def __init__(self):
        super().__init__()

    # Génération d'une grille vierge
    def setVirginGrid(self):
        for l in range(self._steps[0]):
            for c in range(self._steps[1]):
                self._grid[(l, c)] = 0

    # Génération aléatoires de cellules
    def generateRandomGrid(self):
        for l in range(self._steps[0]):
            for c in range(self._steps[1]):
                self._grid[(l, c)] = random.choice(self.states)

    # Évolution des cellules
    def evolveGrid(self):
        oldGrid = copy.deepcopy(self._grid)

        for x in self._grid:
            self._grid[x] = self.evalStatut(oldGrid, x)

        return False if self._grid == oldGrid else True

    # Évaluation du statut de la cellules
    def evalStatut(self, grid, coord):
        cells = self.getEvalGrid(grid, coord)
        nbr = cells.count(self._alive)

        if nbr == 3:
            return self._alive

        if nbr == 2:
            return self._alive if self._grid[coord] == self._alive else self._dead

        if nbr < 2 or nbr > 3:
            return self._dead

    # Construction de la grille d'évaluation
    def getEvalGrid(self, grid, coord):
        cells = []

        l = coord[0] - self.influence
        c = coord[1] - self.influence

        while l <= coord[0] + self.influence:
            if l >= 0 and l < self._steps[0]:
                if c >= 0 and c < self._steps[1]:
                    if (l, c) != coord:
                        cells.append(grid[(l, c)])

            if l <= coord[0] + self.influence:
                c += 1
            else:
                c = coord[1] - self.influence
            if c > coord[1] + self.influence:
                l += 1
                c = coord[1] - self.influence

        return cells

    # Définition des dimensions
    def setDimensions(self, sizeL, sizeC):
        self._steps = (sizeL, sizeC)

    # Inversion de l'état de la cellule
    def changeCell(self, l, c):
        self._grid[(l, c)] = self._alive if self._grid[(l, c)] == self._dead else self._dead

    # Déclaration de la position de départ
    def getFirstPos(self, n):
        return n - 1 if n - 1 >= 0 else -1

    # Déclaration de la position de fin
    def getLastPos(self, n, limit):
        return n + 1 if n + 1 < limit else 0