# coding: utf-8

import random
import copy

from models.gridModel import GridModel

class Grid(GridModel):
    def __init__(self, config):
        super().__init__(config)

    # Génération d'une grille
    def newGrid(self, rand = False):
        for l in range(self._steps[0]):
            for c in range(self._steps[1]):
                self._grid[(l, c)] = 0 if rand == False else random.choice(self.states)

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
        cell = [coord[0] - self.influence, coord[1] - self.influence]

        while cell[0] <= coord[0] + self.influence:
            if cell[0] >= 0 and cell[0] < self._steps[0]:
                if cell[1] >= 0 and cell[1] < self._steps[1]:
                    if (cell[0], cell[1]) != coord:
                        cells.append(grid[(cell[0], cell[1])])

            if cell[0] <= coord[0] + self.influence:
                cell[1] += 1
            else:
                cell[1] = coord[1] - self.influence
            if cell[1] > coord[1] + self.influence:
                cell[0] += 1
                cell[1] = coord[1] - self.influence

        return cells

    # Définition des dimensions
    def setDimensions(self, sizeL, sizeC):
        self._steps = (sizeL, sizeC)

    # Appel d'une cellule localisée. Arguments(ligne et cellule) 
    def getCell(self, l, c):
        return self._grid[(l, c)]

    # Inversion de l'état de la cellule
    def changeCell(self, l, c):
        self._grid[(l, c)] = self._alive if self._grid[(l, c)] == self._dead else self._dead

    # Initialisation d'une cellules
    def setCell(self, cell, statut):
        self._grid[cell] = statut