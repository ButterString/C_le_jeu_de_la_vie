# coding: utf-8

from tkinter import Canvas
# import math

class CanvasGame():
    def __init__(self, mainWindow, grid):
        # Fenètre principale
        self.mainWindow = mainWindow
        # Grille
        self.grid = grid
        # Statut de lecture
        self.runLifeGame = False
        # Couleur des cellules vivante
        self.alive = 'green'
        # Couleur des cellules mortes
        self.dead = '#101010'

        # Déclaration de la taille des cellules
        self.cellSize = 30

        # Dimensions du canvas
        w = self.grid.getSizeL() * self.cellSize
        h = self.grid.getSizeC() * self.cellSize

        # Déclaration du canvas
        self.canvas = Canvas(self.mainWindow, width=w, height=h, bg=self.dead)
        self.canvas.pack()

    # Fonctions de génération de la grille
    def drawGrid(self):
        # Initialisation des coordonnées verticales
        y0 = 0
        y1 = self.cellSize

        # lecture des lignes
        for l in range(self.grid.getSizeL()):
            # Initialisation des coordonnées horizontales
            x0 = 0
            x1 = self.cellSize

            # lecture des colones
            for c in range(self.grid.getSizeC()):
                # Initialisation de l'état de la cellule
                cell = self.dead if self.grid.getCell(l, c) < 1 else self.alive
                # Création de la cellule
                self.canvas.create_oval(x0, y0, x1, y1, width = 0, fill = cell)

                # modification des coordonnées horizontales
                x0 += self.cellSize
                x1 += self.cellSize

            # modification des coordonnées verticales
            y0 += self.cellSize
            y1 += self.cellSize

    # Fonction d'édition du statut de lecture
    def setPlayStatut(self, statut):
        self.runLifeGame = statut

    # Fonction de mise à jour de la grille
    def update(self):
        # Si le jeu set en lecture
        if self.runLifeGame == True:
            # Définition de l'état de lecture
            self.runLifeGame = self.grid.evolveGrid()

        # Nettoyage du canvas
        self.clearCanvas()
        # Création de la grille
        self.drawGrid()

    # Fonction de mise à jour de la grille
    def canvasLoop(self):
        # Mise à jour de la grille
        self.update()
        # Si l'état du jeu est en lecture
        if self.runLifeGame == True:
            # Lecture
            self.canvas.after(250, self.canvasLoop)

    # Fonction de nettoyage du canvas
    def clearCanvas(self):
        self.canvas.delete('all')