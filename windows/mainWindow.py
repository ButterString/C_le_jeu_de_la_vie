# coding: utf-8

import sys
import tkinter
from tkinter import *

class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0, 0)
        self.configure(background = 'black')
        # self.attributes('-alpha', 0.75)
        self.title('Life Game')
        self.geometry('900x900')
    
    def leaveProg(self):
        sys.exit()