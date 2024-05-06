# coding: utf-8

from tkinter import Canvas
import math

from canvasGrids.cells import Cells

class CanvasGame():
    def __init__(self, mainWindow, grid):
        # Grille
        self.grid = grid
        # Statut de lecture
        self.runLifeGame = False

        # Déclaration du canvas
        self.canvas = Canvas(mainWindow, width=900, height=900, bg='black')
        self.canvas.pack()

    # Fonctions de génération de la grille
    def drawGrid(self):
        Cells(self.canvas, self.grid)

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
    
    # Fonction d'évènement
    def bindCanvas(self):
        self.canvas.bind('<Button-1>', self.cellChange)
    
    def cellChange(self, event):
        c = math.floor(event.x / self.grid.getSizeC())
        l = math.floor(event.y / self.grid.getSizeL())
        self.grid.changeCell(l, c)
        self.update()