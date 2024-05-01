# coding: utf-8

import random
import copy
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
        self.grid = []

        # lecture des lignes
        for l in range(self.sizeL):
            # Génération d'une liste vide dans chaque ligne
            l = []

            # Lecture des colones
            for c in range(self.sizeC):
                # Génération aléatoires de cellules
                l.append(random.choice(self.states))
            
            # Ajout de la ligne à la grille
            self.grid.append(l)
    
    # Fonction d'évolution des cellules
    def evolveGrid(self):
        oldGrid = copy.deepcopy(self.grid)

        l = 0
        c = 0

        # Lecture des lignes
        while c < self.sizeC:
            cells = []

            startC = c - 1 if c - 1 >= 0 else c
            endC = c + 2 if c + 1 < self.sizeC else c + 1

            startL = l - 1 if l - 1 >= 0 else l
            endL = l + 2 if l + 1 < self.sizeL else l + 1

            for line in oldGrid[startL:endL]:
                if line == oldGrid[l]:
                    if c - 1 >= 0:
                        cells.append(line[c-1])
                    if c + 1 < self.sizeC:
                        cells.append(line[c+1])
                else:
                    cells += line[startC:endC]
            
            self.grid[l][c] = self.evalStatut(oldGrid[l][c], cells)
            
            c += 1
            if c == self.sizeC:
                l += 1
                c = 0
            if l == self.sizeL:
                c = self.sizeC
        
        return False if self.grid == oldGrid else True
    
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