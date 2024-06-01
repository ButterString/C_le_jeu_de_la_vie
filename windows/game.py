# coding: utf-8

from tkinter import Canvas
import math

from models.gameModel import GameModel

class Game(GameModel):
    def __init__(self):
        super().__init__()

    # Génération d'une grille aléatoire
    def randomGame(self):
        self.newGame()
        self.grid.newGrid(True)
        self.canvas.drawGrid(self.grid)

    # Chargement d'une grille
    def loadGame(self):
        self.newGame()
        self.nameGrid = self.datas.findJson()

        if self.nameGrid != False:
            self.grid.grid = self.datas.loadGrid(self.nameGrid)
            self.canvas.drawGrid(self.grid)

    # Création d'une grille
    def createGame(self):
        self.newGame()
        self.grid.newGrid()
        self.canvas.drawGrid(self.grid)
        self.bind('<Button-1>', self.eventGame)

    # Gestion de l'évènement
    def eventGame(self, event):
        l = math.floor(event.y / self.grid.steps[0])
        c = math.floor(event.x / self.grid.steps[1])

        self.grid.changeCell(l, c)
        self.canvas.drawGrid(self.grid)

    # Backup de la grille
    def backupGame(self):
        self.stopGame()
        f = self.datas.saveGrid(self.grid.grid)

        if f != False:
            self.nameGrid = f
            self.datas.writeGrid(self.nameGrid, self.grid.grid)

    # sauvegarde de la grille
    def saveGame(self):
        self.stopGame()

        if self.nameGrid == "":
            self.backupGame()
        else:
            self.datas.writeGrid(self.nameGrid, self.grid.grid)