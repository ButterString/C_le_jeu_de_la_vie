# coding: utf-8

from windows.gameGrid import GameGrid
from grids.grille import Grille

if __name__ == '__main__':
    frame = GameGrid(Grille())
    frame.mainloop()