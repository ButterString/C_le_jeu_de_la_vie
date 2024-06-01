# coding: utf-8

from models.windowModel import WindowModel
from windows.canvasGame import CanvasGame
from windows.menuBar import MenuBar
from grids.grid import Grid
from bridges.datasBridge import DatasBridge

class GameModel(WindowModel):
    def __init__(self):
        # Initialisation du model
        super().__init__()
        # Déclaration des données
        self.datas = DatasBridge()
        # Récupération de la configuration
        config = self.datas.jsonRead("configGame")
        # Définition du répertoire des grille
        self.datas.directory = config["gridsDir"]

        """
        Configuration de la fenètre
        """
        # Redimensionnement de la fenètre
        self.resizable(0, 0)
        # Titre de la fenètre
        self.title(config["title"])
        # Icone de la fenètre
        self.iconbitmap(config["icone"])
        # Alpha de la fenètre
        self.attributes('-alpha', config["alpha"])
        # Background de la fenètre
        self.configure(background = config["background"])
        # Dimensions de la fenètre
        self.geometry(config["dimensions"])

        """
        Configuration des dépendances
        """
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