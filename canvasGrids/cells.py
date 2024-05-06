# coding: utf-8

class Cells():
    def __init__(self, canvas, grid):
        # Couleur des cellules vivante
        alive = 'white'
        # Couleur des cellules mortes
        dead = 'black'

        # Déclaration de la taille des cellules
        stepX = int(canvas.winfo_width() / grid.getSizeC())
        stepY = int(canvas.winfo_height() / grid.getSizeL())

        y0 = 0
        y1 = stepY

        for l in range(stepY):
            x0 = 0
            x1 = stepX

            for c in range(stepX):
                cell = dead if grid.getCell(l, c) < 1 else alive
                canvas.create_oval(x0, y0, x1, y1, width=0, fill=cell)

                x0 += stepX
                x1 += stepX
            
            y0 += stepY
            y1 += stepY