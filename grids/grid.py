# coding: utf-8

import random
import copy

class Grid():
    def __init__(self):
        # Dimensions par défaut
        self.sizeL = 30
        self.sizeC = 30
        # valeur des cellules vivantes
        self.alive = 1
        # valeur des cellules mortes
        self.dead = 0
        # Tableau des états des cellules (pour la génération aléatoire)
        self.states = [self.alive, self.dead]
        # Déclaration du rayon d'influence
        self.influence = 3

    # Génération d'une grille vierge
    def setVirginGrid(self):
        # Initialisation de la grille
        self.grid = []
        for l in range(self.sizeL):
            line = []
            for c in range(self.sizeC):
                line.append(0)
            self.grid.append(line)

    # Génération aléatoires de cellules
    def generateRandomGrid(self):
        self.setVirginGrid()
        for l in range(self.sizeL):
            for c in range(self.sizeC):
                cell = random.choice(self.states)
                self.grid[l][c] = cell

    # Chargement d'une grille
    def setGrid(self, grid):
        self.grid = grid
    
    # Évolution des cellules
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

    # Construction de la grille d'évaluation
    def getEvalGrid(self, grid, l, c):
        cells = []

        lines = [self.getFirstPos(l), l, self.getLastPos(l, self.sizeL)]

        for line in lines:
            cells.append(grid[line][self.getFirstPos(c)])
            if line != l:
                cells.append(grid[line][c])
            cells.append(grid[line][self.getLastPos(c, self.sizeC)])

        return cells

    # Évaluation du statut de la cellules
    def evalStatut(self, statut, cells):
        nbr = cells.count(self.alive)

        if nbr == 3:
            return self.alive

        if nbr == 2:
            return self.alive if statut == self.alive else self.dead

        if nbr < 2 or nbr > 3:
            return self.dead
    
    # Définition des dimensions
    def setDimensions(self, sizeL, sizeC):
        self.sizeL = sizeL
        self.sizeC = sizeC
    
    # Inversion de l'état de la cellule
    def changeCell(self, l, c):
        self.grid[l][c] = self.alive if self.grid[l][c] == self.dead else self.dead
    
    # Déclaration de la position de départ
    def getFirstPos(self, n):
        return n - 1 if n - 1 >= 0 else -1

    # Déclaration de la position de fin
    def getLastPos(self, n, limit):
        return n + 1 if n + 1 < limit else 0

    # Appel du nombre de ligne
    def getSizeL(self):
        return self.sizeL

    # Appel du nombre de colonnes
    def getSizeC(self):
        return self.sizeC

    # Appel d'une cellule localisée. Arguments(ligne et cellule) 
    def getCell(self, l, c):
        return self.grid[l][c]
    
    # Appel de la grille
    def getGrid(self):
        return self.grid