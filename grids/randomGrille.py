# coding: utf-8

import random
from grids.grille import Grille

class RandomGrille(Grille):
    def __init__(self):
        super().__init__()
        
        # Génération aléaloire de cellules
        self.generateRandomGrid()

    # Fonction de génération aléatoires de cellules
    def generateRandomGrid(self):
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