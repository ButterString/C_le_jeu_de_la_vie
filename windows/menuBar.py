# coding: utf-8

from tkinter import Menu
from tkinter.filedialog import askopenfilename

class MenuBar():
    def __init__(self, mainWindow):
        menuBar = Menu(mainWindow)

        menuGame = Menu(menuBar, tearoff=0)

        menuGame.add_command(label="Random", command=mainWindow.randomGame)
        menuGame.add_command(label="Load", command=mainWindow.loadGame)
        menuGame.add_separator()
        menuGame.add_command(label="Create Game", command=mainWindow.createGame)
        menuGame.add_separator()
        menuGame.add_command(label="Save", command=mainWindow.saveGame)
        menuGame.add_command(label="Save As", command=mainWindow.backupGame)
        menuGame.add_separator()
        menuGame.add_command(label="Quit", command=mainWindow.leaveProg)
        
        menuBar.add_cascade(label="Game", menu=menuGame)
        menuBar.add_separator()
        menuBar.add_command(label="Run", command=mainWindow.startGame)
        menuBar.add_command(label="stop", command=mainWindow.stopGame)

        mainWindow.config(menu=menuBar)