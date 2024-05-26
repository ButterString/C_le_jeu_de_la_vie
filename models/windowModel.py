# coding: utf-8

import sys
import tkinter
from tkinter import *

class WindowModel(tkinter.Tk):
    def __init__(self, config):
        super().__init__()

        self.resizable(0, 0)
        # self.title('Life Game')
        self.title(config["title"])
        self.iconbitmap(config["icone"])
        # self.attributes('-alpha', 0.75)
        self.attributes('-alpha', 0.75)
        # self.configure(background = 'black')
        self.configure(background = config["background"])
        # self.geometry('900x900')
        self.geometry(config["dimensions"])
    
    def leaveProg(self):
        sys.exit()