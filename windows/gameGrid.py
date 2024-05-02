# coding: utf-8

from tkinter import Canvas
# import math

from datas.jsonDatas import JsonDatas
from windows.mainWindow import MainWindow
from windows.canvasGame import CanvasGame
from windows.menuBar import MenuBar

class GameGrid(MainWindow):
    def __init__(self, grid):
        super().__init__()
        self.datas = JsonDatas()

        # Déclaration de la liste des cellules
        self.grid = grid
        # Déclaration de la taille des cellules
        self.cellSize = 30
        
        # Dimensions du canvas
        w = self.grid.getSizeL() * self.cellSize
        h = self.grid.getSizeC() * self.cellSize
    
        # Déclaration du canvas
        self.canvas = CanvasGame(self, self.grid, w, h)

        # Initialisation de la barre de menu
        self.menuBar = MenuBar(self)
    
    def randomLifeGame(self):
        self.grid.generateRandomGrid()
        self.canvas.canvasClear()
        self.startGame()
    
    def customGame(self):
        fileGrid = self.datas.loadJson()
        self.grid.customGrid(fileGrid)
        self.startGame()
    
    def startGame(self):
        self.canvas.setPlayStatut(True)
        self.canvas.canvasLoop()
    
    def stopGame(self):
        self.canvas.setPlayStatut(False)
        self.canvas.canvasLoop()