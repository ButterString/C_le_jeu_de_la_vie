# coding: utf-8

import random
import copy

from models.gridModel import GridModel

class Grid(GridModel):
    def __init__(self):
        super().__init__()

    # Génération d'une grille vierge
    def setVirginGrid(self):
        self._grid = []
        for l in range(self._sizeL):
            line = []
            for c in range(self._sizeC):
                line.append(0)
            self._grid.append(line)

    # Génération aléatoires de cellules
    def generateRandomGrid(self):
        self.setVirginGrid()
        for l in range(self._sizeL):
            for c in range(self._sizeC):
                cell = random.choice(self.states)
                self._grid[l][c] = cell

    # Évolution des cellules
    def evolveGrid(self):
        oldGrid = copy.deepcopy(self._grid)

        l = 0
        c = 0

        while c < self._sizeC:
            cells = self.getEvalGrid(oldGrid, l, c)

            self._grid[l][c] = self.evalStatut(oldGrid[l][c], cells)

            c += 1
            if c == self._sizeC:
                l += 1
                c = 0
            if l == self._sizeL:
                c = self._sizeC

        return False if self._grid == oldGrid else True

    # Construction de la grille d'évaluation
    def getEvalGrid(self, grid, l, c):
        cells = []

        lines = [self.getFirstPos(l), l, self.getLastPos(l, self._sizeL)]

        for line in lines:
            cells.append(grid[line][self.getFirstPos(c)])
            if line != l:
                cells.append(grid[line][c])
            cells.append(grid[line][self.getLastPos(c, self._sizeC)])

        return cells

    # Évaluation du statut de la cellules
    def evalStatut(self, statut, cells):
        nbr = cells.count(self._alive)

        if nbr == 3:
            return self._alive

        if nbr == 2:
            return self._alive if statut == self._alive else self._dead

        if nbr < 2 or nbr > 3:
            return self._dead

    # Définition des dimensions
    def setDimensions(self, _sizeL, _sizeC):
        self._sizeL = _sizeL
        self._sizeC = _sizeC

    # Inversion de l'état de la cellule
    def changeCell(self, l, c):
        self._grid[l][c] = self._alive if self._grid[l][c] == self._dead else self._dead

    # Déclaration de la position de départ
    def getFirstPos(self, n):
        return n - 1 if n - 1 >= 0 else -1

    # Déclaration de la position de fin
    def getLastPos(self, n, limit):
        return n + 1 if n + 1 < limit else 0