# coding: utf-8

import random
import copy
from tkinter.filedialog import asksaveasfile

from datas.jsonDatas import JsonDatas

class Grille():
    def __init__(self):
        self.datas = JsonDatas()

        self.grid = self.loadEmptyGrid()

        # Nombre de lignes
        self.sizeL = len(self.grid)
        # Nombre de colonnes
        self.sizeC = len(self.grid[0])
        # valeur des cellules vivantes
        self.alive = 1
        # valeur des cellules mortes
        self.dead = 0
        # Tableau des états des cellules (pour la génération aléatoire)
        self.states = [self.alive, self.dead]
        # Déclaration du rayon d'influence
        self.influence = 3

    def loadEmptyGrid(self):
        return self.datas.jsonRead("emptyGrid")

    def loadCustomGrid(self):
        startGrid = self.datas.findJson(
            self.datas.loadJson()
        )

        if startGrid != None:
            self.grid = startGrid

    # Fonction de génération aléatoires de cellules
    def generateRandomGrid(self):
        # lecture des lignes
        for l in range(self.sizeL):
            # Lecture des colones
            for c in range(self.sizeC):
                # Génération aléatoires de cellule
                cell = random.choice(self.states)
                self.grid[l][c] = cell

        # Sauvegarde de la grille
        self.datas.writeJson(self.grid)

    # Fonction d'évolution des cellules
    def evolveGrid(self):
        oldGrid = copy.deepcopy(self.grid)

        l = 0
        c = 0

        # Lecture des lignes
        while c < self.sizeC:
            cells = self.getEvalGrid(oldGrid, l, c)

            self.grid[l][c] = self.evalStatut(oldGrid[l][c], cells)

            c += 1
            if c == self.sizeC:
                l += 1
                c = 0
            if l == self.sizeL:
                c = self.sizeC

        return False if self.grid == oldGrid else True

    # Fonction de construction de la grille d'évaluation
    def getEvalGrid(self, grid, l, c):
        cells = []

        lines = [self.getFirstPos(l), l, self.getLastPos(l, self.sizeL)]

        for line in lines:
            cells.append(grid[line][self.getFirstPos(c)])
            if line != l:
                cells.append(grid[line][c])
            cells.append(grid[line][self.getLastPos(c, self.sizeC)])

        return cells
    
    # Fonction de déclaration de la position de départ
    def getFirstPos(self, n):
        return n - 1 if n - 1 >= 0 else -1

    # Fonction de déclaration de la position de fin
    def getLastPos(self, n, limit):
        return n + 1 if n + 1 < limit else 0

    # Fonction d'évaluation du statut de la cellules
    def evalStatut(self, statut, cells):
        nbr = cells.count(self.alive)

        if nbr == 3:
            return self.alive

        if nbr == 2:
            return self.alive if statut == self.alive else self.dead

        if nbr < 2 or nbr > 3:
            return self.dead

    # Fonction d'appel d'une cellule localisée. Arguments(ligne et cellule) 
    def getCell(self, l, c):
        return self.grid[l][c]

    # Fonction d'appel du nombre de ligne
    def getSizeL(self):
        return self.sizeL

    # Fonction d'appel du nombre de colonnes
    def getSizeC(self):
        return self.sizeC