# coding: utf-8

import random
import copy
from tkinter.filedialog import asksaveasfile

from datas import Datas

class Grille():
    def __init__(self):
        self.datas = Datas()

        startGrid = self.loadGrid()

        # Nombre de lignes
        self.sizeL = len(startGrid)
        # Nombre de colonnes
        self.sizeC = len(startGrid[0])
        # couleur des cellules vivante
        self.alive = 'green'
        # couleur des cellules mortes
        self.dead = '#101010'
        # Tableau des états des cellules (pour la génération aléatoire)
        self.states = [self.alive, self.dead]
        # Déclaration du rayon d'influence
        self.influence = 3
        
        #  Génération des cellules
        self.generateGrid(startGrid)
    
    def loadGrid(self):
        return self.datas.datasRead("emptyGrid")
    
    def customGrid(self, fileGrid):
        startGrid = self.datas.findDatas(fileGrid)
        self.generateGrid(startGrid)
    
    def generateGrid(self, startGrid):
        self.grid = []

        # lecture des lignes
        for l in startGrid:
            line = []
            for c in l:
                line.append(self.alive if c == 1 else self.dead)
            self.grid.append(line)

    # Fonction de génération aléatoires de cellules
    def generateRandomGrid(self):
        jsonGrid = []

        # lecture des lignes
        for l in range(self.sizeL):
            # Génération d'une liste vide dans chaque ligne
            l = []

            # Lecture des colones
            for c in range(self.sizeC):
                # Génération aléatoires de cellule
                l.append(random.choice([0, 1]))
            
            # Ajout de la ligne à la grille
            jsonGrid.append(l)
        
        self.datas.writeDatas(jsonGrid)
        self.generateGrid(jsonGrid)
    
    # Fonction d'évolution des cellules
    def evolveGrid(self):
        oldGrid = copy.deepcopy(self.grid)

        l = 0
        c = 0

        # Lecture des lignes
        while c < self.sizeC:
            cells = []

            lines = [self.getFirstPos(l), l, self.getLastPos(l, self.sizeL)]

            for line in lines:
                cells.append(oldGrid[line][self.getFirstPos(c)])
                if line != l:
                    cells.append(oldGrid[line][c])
                cells.append(oldGrid[line][self.getLastPos(c, self.sizeC)])
            
            self.grid[l][c] = self.evalStatut(oldGrid[l][c], cells)
            
            c += 1
            if c == self.sizeC:
                l += 1
                c = 0
            if l == self.sizeL:
                c = self.sizeC
        
        return False if self.grid == oldGrid else True
    
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