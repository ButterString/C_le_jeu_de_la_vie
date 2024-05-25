# coding: utf-8

from tkinter import Canvas

class CanvasGame():
    def __init__(self, mainWindow):
        # Couleur des cellules vivante
        self.alive = 'white'
        # Couleur des cellules mortes
        self.dead = 'black'
        # Dimensions
        self.setDimensions(900, 900)

        # Déclaration du canvas
        self.canvas = Canvas(mainWindow, width=self.sizeW, height=self.sizeH, bg='black')
        self.canvas.pack()

    # Fonctions de génération de la grille
    def drawGrid(self, grid):
        # Nettoyage du canvas
        self.canvas.delete('all')

        # Dimensions
        lines = int(self.sizeH / grid.steps[0])
        cols = int(self.sizeW / grid.steps[1])

        l = 0
        c = 0

        while l < grid.steps[0]:
            # Définition de la cellule
            cell = self.dead if grid.grid[(l, c)] < 1 else self.alive

            # Création de la cellule
            x0 = c * cols
            y0 = l * lines
            x1 = x0 + cols
            y1 = y0 + lines
            self.canvas.create_oval(x0, y0, x1, y1, width=0, fill=cell)

            c += 1

            if c == grid.steps[1]:
                c = 0
                l += 1

    # Dimensions du canvas
    def setDimensions(self, w, h):
        self.sizeW = w
        self.sizeH = h

    # Édition du canvas
    def getCanvas(self):
        return self.canvas
