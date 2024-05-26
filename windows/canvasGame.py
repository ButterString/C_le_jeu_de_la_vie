# coding: utf-8

from models.canvasModel import CanvasModel

class CanvasGame(CanvasModel):
    def __init__(self, mainWindow, config):
        super().__init__(mainWindow, config)

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
            x = c * cols
            y = l * lines

            # Définition de la cellule
            cell = self.dead if grid.grid[(l, c)] < 1 else self.alive
            # Création de la cellule
            coords = [x, y, x + cols, y + lines]
            self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3], width=0, fill=cell)

            c += 1

            if c == grid.steps[1]:
                c = 0
                l += 1