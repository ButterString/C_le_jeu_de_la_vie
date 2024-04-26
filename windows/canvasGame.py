# coding: utf-8

from tkinter import Canvas
import math

class CanvasGame():
    def __init__(self, mainWindow, grid, w, h):
        self.grid = grid
        self.mainWindow = mainWindow
        self.runLifeGame = False

        # Déclaration du canvas
        self.canvas = Canvas(self.mainWindow, width=w, height=h)
        self.canvas.pack()

        # Génération de la grille
        self.drawGrid()
    
    # Fonctions de génération de la grille
    def drawGrid(self):
        y0 = 0
        y1 = self.grid.getSizeL()

        # lecture des lignes
        for l in range(self.grid.getSizeL()):
            x0 = 0
            x1 = self.grid.getSizeC()
            
            # lecture des colones
            for c in range(self.grid.getSizeC()):
                cell = self.grid.getCell(l, c)
                self.canvas.create_rectangle(x0, y0, x1, y1, width = 1, fill = cell)

                x0 += self.grid.getSizeC()
                x1 += self.grid.getSizeC()

            y0 += self.grid.getSizeL()
            y1 += self.grid.getSizeL()
    
    def canvasClear(self):
        self.canvas.delete('all')
        self.drawGrid()
    
    def setPlayStatut(self, statut):
        self.runLifeGame = statut
    
    # Fonction de mise à jour de la grille
    def update(self):
        self.grid.evolveGrid()
        self.canvasClear()
        self.drawGrid()

    # Fonction de mise à jour de la grille
    def canvasLoop(self):
        self.update()
        if self.runLifeGame == True:
            self.canvas.after(400, self.canvasLoop)