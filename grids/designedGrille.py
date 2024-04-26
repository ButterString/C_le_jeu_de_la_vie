# coding: utf-8

import random
from grids.grille import Grille

class DesignedGrille(Grille):
    def __init__(self, startGrid="emptyGrid"):
        super().__init__()
        
        #  Génération des cellules
        self.generateDefineGrid(startGrid)
    
    def generateDefineGrid(self, startGrid):
        # lecture des lignes
        for l in startGrid:
            line = []
            for c in l:
                line.append(self.alive if c == 1 else self.dead)
            self.grid.append(line)