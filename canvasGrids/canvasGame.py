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
        cols = int(self.sizeW / len(grid[0]))
        lines = int(self.sizeH / len(grid))

        # Coordonnées verticales
        y0 = 0
        y1 = lines

        # Lecture des lignes
        for l in range(lines):
            # Coordonnées horizontales
            x0 = 0
            x1 = cols

            # Lecture des colonnes
            for c in range(cols):
                # Définition de la cellule
                cell = self.dead if grid[l][c] < 1 else self.alive
                # Création de la cellule
                self.canvas.create_oval(x0, y0, x1, y1, width=0, fill=cell)

                # Évolution des positions horizontales
                x0 += cols
                x1 += cols

            # Évolution des positions verticales
            y0 += lines
            y1 += lines

    # Dimensions du canvas
    def setDimensions(self, w, h):
        self.sizeW = w
        self.sizeH = h

    # Édition du canvas
    def getCanvas(self):
        return self.canvas
