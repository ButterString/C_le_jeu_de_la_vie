# coding: utf-8

from tkinter import Menu
from tkinter.filedialog import askopenfilename
from functools import partial

class MenuBar():
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        self.menuBar = Menu(self.mainWindow)

        self.menuBar.add_command(label="Grille aléatoire", command=self.mainWindow.randomLifeGame)
        self.menuBar.add_command(label="Charger une grille", command=self.mainWindow.customGame)
        self.menuBar.add_command(label="Run", command=self.mainWindow.startGame)
        self.menuBar.add_command(label="stop", command=self.mainWindow.stopGame)

        self.mainWindow.config(menu=self.menuBar)