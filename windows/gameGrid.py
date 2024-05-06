# coding: utf-8

from windows.mainWindow import MainWindow
from canvasGrids.canvasGame import CanvasGame
from windows.menuBar import MenuBar
from grids.grille import Grille

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
        # Génération d'une grille aléatoire
        self.grid.generateRandomGrid()
        # Lancement du jeu
        self.startGame()

    def loadGame(self):
        # Chargement d'une grille enregistrée
        self.grid.loadCustomGrid()
        # Lancement du jeu
        self.startGame()

    def startGame(self):
        # Modification du statut de lecture
        self.canvas.setPlayStatut(True)
        # Lecture du jeu
        self.canvas.canvasLoop()

    def stopGame(self):
        # Modification du statut de lecture
        self.canvas.setPlayStatut(False)
        # Arrêt du jeu
        self.canvas.canvasLoop()