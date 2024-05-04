# coding: utf-8

from tkinter import Canvas
import math

class CanvasGame():
    def __init__(self, mainWindow, grid):
        self.grid = grid
        self.mainWindow = mainWindow
        self.runLifeGame = False
        # couleur des cellules vivante
        self.alive = 'green'
        # couleur des cellules mortes
        self.dead = '#101010'
        
        # Déclaration de la taille des cellules
        self.cellSize = 30
        
        # Dimensions du canvas
        w = self.grid.getSizeL() * self.cellSize
        h = self.grid.getSizeC() * self.cellSize

        # Déclaration du canvas
        self.canvas = Canvas(self.mainWindow, width=w, height=h, bg=self.dead)
        self.canvas.pack()

        # Génération de la grille
        self.drawGrid()
    
    # Fonctions de génération de la grille
    def drawGrid(self):
        y0 = 0
        y1 = self.cellSize

        # lecture des lignes
        for l in range(self.grid.getSizeL()):
            x0 = 0
            x1 = self.cellSize
            
            # lecture des colones
            for c in range(self.grid.getSizeC()):
                cell = self.dead if self.grid.getCell(l, c) < 1 else self.alive
                self.canvas.create_oval(x0, y0, x1, y1, width = 0, fill = cell)

                x0 += self.cellSize
                x1 += self.cellSize

            y0 += self.cellSize
            y1 += self.cellSize
    
    def canvasClear(self):
        self.canvas.delete('all')
        self.drawGrid()
    
    def setPlayStatut(self, statut):
        self.runLifeGame = statut
    
    # Fonction de mise à jour de la grille
    def update(self):
        if self.runLifeGame == True:
            self.runLifeGame = self.grid.evolveGrid()
        self.canvasClear()

    # Fonction de mise à jour de la grille
    def canvasLoop(self):
        self.update()
        if self.runLifeGame == True:
            self.canvas.after(250, self.canvasLoop)