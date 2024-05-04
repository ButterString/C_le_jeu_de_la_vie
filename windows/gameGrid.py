# coding: utf-8

from windows.mainWindow import MainWindow
from windows.canvasGame import CanvasGame
from windows.menuBar import MenuBar

class GameGrid(MainWindow):
    def __init__(self, grid):
        super().__init__()

        # Déclaration de la liste des cellules
        self.grid = grid
        # Déclaration du canvas
        self.canvas = CanvasGame(self, self.grid)
        # Initialisation de la barre de menu
        self.menuBar = MenuBar(self)
    
    def randomLifeGame(self):
        self.grid.generateRandomGrid()
        self.canvas.canvasClear()
        self.startGame()
    
    def loadGame(self):
        self.grid.loadCustomGrid()
        self.startGame()
    
    def startGame(self):
        self.canvas.setPlayStatut(True)
        self.canvas.canvasLoop()
    
    def stopGame(self):
        self.canvas.setPlayStatut(False)
        self.canvas.canvasLoop()