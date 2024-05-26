# coding: utf-8

from tkinter import Canvas
import math

from models.windowModel import WindowModel
from windows.canvasGame import CanvasGame
from windows.menuBar import MenuBar
from grids.grid import Grid
from datas.jsonDatas import JsonDatas

class Game(WindowModel):
    def __init__(self):
        # Déclaration des données
        self.datas = JsonDatas()
        # Récupération de la configuration
        config = self.datas.jsonRead("configGame")
        self.datas.directory = config["datas"]["grids"]
        # Initialisation du model
        super().__init__( config["canvas"])

        # Déclaration de la grille
        self.grid = Grid(config["grid"])
        # Déclaration du canvas
        self.canvas = CanvasGame(self, config["canvas"])
        # Initialisation de la barre de menu
        self.menuBar = MenuBar(self)
        # Statut de lecture
        self.play = False
        # Nom de la grille
        self.nameGrid = ""

    # Génération d'une grille aléatoire
    def randomGame(self):
        self.newGame()
        self.grid.newGrid(True)
        self.canvas.drawGrid(self.grid)

    # Chargement d'une grille
    def loadGame(self):
        self.newGame()
        self.nameGrid = self.datas.loadJson()

        if self.nameGrid != False:
            self.grid.grid = self.convertGrid(self.datas.findJson(self.nameGrid), False)
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
        f = self.datas.saveJson(self.convertGrid(self.grid.grid))
        if f != False:
            self.nameGrid = f

    # sauvegarde de la grille
    def saveGame(self):
        self.stopGame()

        if self.nameGrid == "":
            self.backupGame()
        else:
            self.datas.writeJson(self.nameGrid, self.convertGrid(self.grid.grid))

    # Convertion grid<=>json
    def convertGrid(self, grid, toJson = True):
        gridBackup = {}

        for x in grid:
            coords = ":".join(map(str, x)) if toJson == True else tuple(map(int, x.split(":")))
            gridBackup[coords] = grid[x]

        return gridBackup

    # Nouveau jeu
    def newGame(self):
        self.stopGame()
        self.nameGrid = ""

    # Lancement du jeu
    def startGame(self):
        self.unbind('<Button-1>')
        self.statut = True
        self.playGame()

    # Arrêt du jeu
    def stopGame(self):
        self.statut = False

    # Lecture du jeu
    def playGame(self):
        if self.statut == True:
            self.statut = self.grid.evolveGrid()
            self.canvas.drawGrid(self.grid)
            self.after(250, self.playGame)