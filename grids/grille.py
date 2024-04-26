# coding: utf-8

import random
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
        # Lecture des lignes
        for l in range(self.sizeL):
            # Lecture des colonnes
            for c in range(self.sizeL):
                # Vérification du statut de la cellules
                self.setCellStatut(l, c)
    
    # Fonction de vérification de l'état de la cellule. Arguments(ligne et cellule)
    def setCellStatut(self, l, c):
        # Liste vide des cellules voisines
        self.eval = []
        # Liste de l'état actuel des cellules
        oldGrid = self.grid[:]
        # Liste vide des lignes à évaluer
        lines = []

        # Récupération des indices des ligne à évaluer
        if l - 1 >= 0:
            lines.append(l - 1)
        lines.append(l)
        if l + 1 < self.sizeL:
            lines.append(l + 1)

        # évaluation des cellules
        for n in lines:
            if c - 1 >= 0:
                self.eval.append(oldGrid[n][self.getStart(c)])
            if n != l:
                self.eval.append(oldGrid[n][c])
            if c + 1 < self.sizeL:
                self.eval.append(oldGrid[n][self.getEnd(c)])

        # Si la cellule est vivante et qu'elle a deux voisines vivantes
        if self.eval.count(self.alive) == 2 and self.grid[l][c] == self.alive:
            # La cellule est en vie
            self.grid[l][c] = self.alive
        
        # Si la cellule a 3 voisines vivantes (Quelque soit son état)
        if self.eval.count(self.alive) == 3:
            # La cellule est en vie
            self.grid[l][c] = self.alive
        
        # Si il y a moins de 2 cellules ou plus de 3 cellules voisines vivantes
        if self.eval.count(self.alive) < 2 or self.eval.count(self.alive) > 3:
            # La cellules meurt
            self.grid[l][c] = self.dead
        
    # Fonction de définition de la première cellules voisine
    def getStart(self, n):
        start = n - 1
        return start if start >= 0 else self.sizeL - 1
    
    # Fonction de définition de la dernière cellules voisine
    def getEnd(self, n):
        end = n + 1
        return end if end < self.sizeL else self.sizeL - end
    
    # Fonction d'appel de la liste des cellules
    def getGrid(self):
        return self.grid
    
    # Fonction d'appel d'une cellule localisée. Arguments(ligne et cellule) 
    def getCell(self, l, c):
        return self.grid[l][c]
    
    def reverseCell(self, l, c):
        self.grid[l][c] = self.alive if self.grid[l][c] == self.dead else self.dead

    # Fonction d'appel du nombre de ligne
    def getSizeL(self):
        return self.sizeL
    
    # Fonction d'appel du nombre de colonnes
    def getSizeC(self):
        return self.sizeC