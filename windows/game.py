# coding: utf-8

from tkinter import Canvas
import math

from windows.mainWindow import MainWindow
from canvasGrids.canvasGame import CanvasGame
from windows.menuBar import MenuBar
from grids.grid import Grid
from datas.jsonDatas import JsonDatas

class Game(MainWindow):
    def __init__(self):
        super().__init__()
        # Déclaration des données
        self.datas = JsonDatas()
        # Déclaration de la grille
        self.grid = Grid()
        # Déclaration du canvas
        self.canvas = CanvasGame(self)
        # Initialisation de la barre de menu
        self.menuBar = MenuBar(self)
        # Statut de lecture
        self.play = False
        # Nom de la grille
        self.nameGrid = ""

    # Génération d'une grille aléatoire
    def randomGame(self):
        self.newGame()
        self.grid.generateRandomGrid()
        self.canvas.drawGrid(self.grid.grid)

    # Chargement d'une grille
    def loadGame(self):
        self.newGame()
        self.nameGrid = self.datas.loadJson()
        if self.nameGrid != False:
            self.grid.grid(self.datas.findJson(self.nameGrid))
            self.canvas.drawGrid(self.grid.grid)

    # Création d'une grille
    def createGame(self):
        self.newGame()
        self.grid.setVirginGrid()
        self.canvas.drawGrid(self.grid.grid)
        self.bind('<Button-1>', self.eventGame)
        self.editGame()

    # Gestion de l'évènement
    def eventGame(self, event):
        l = math.floor(event.y / self.grid.sizeL)
        c = math.floor(event.x / self.grid.sizeC)

        self.grid.changeCell(l, c)
        self.canvas.drawGrid(self.grid.grid)

    # Backup de la grille
    def backupGame(self):
        self.stopGame()

        f = self.datas.saveJson(self.grid.grid)
        if f != False:
            self.nameGrid = f

    # sauvegarde de la grille
    def saveGame(self):
        self.stopGame()

        if self.nameGrid == "":
            self.backupGame()
        else:
            self.datas.writeJson(self.nameGrid, self.grid.grid)
    
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
            self.canvas.drawGrid(self.grid.grid)
            self.after(250, self.playGame)