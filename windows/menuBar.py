# coding: utf-8

from tkinter import Menu
from tkinter.filedialog import askopenfilename
from functools import partial

class MenuBar():
    def __init__(self, mainWindow):
        menuBar = Menu(mainWindow)

        menuGrid = Menu(menuBar, tearoff=0)

        menuGrid.add_command(label="Grille aléatoire", command=mainWindow.randomLifeGame)
        menuGrid.add_command(label="Charger une grille", command=mainWindow.customGame)
        
        menuBar.add_cascade(label="Grids", menu=menuGrid)
        menuBar.add_command(label="Run", command=mainWindow.startGame)
        menuBar.add_command(label="stop", command=mainWindow.stopGame)
        menuBar.add_command(label="Quit".rjust(250), command=mainWindow.leaveProg)

        mainWindow.config(menu=menuBar)