# coding: utf-8

import sys
import tkinter
from tkinter import *

class WindowModel(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # self.resizable(0, 0)
        # self.title('Life Game')
        # self.attributes('-alpha', 0.75)
        # self.configure(background = 'black')
        # self.geometry('900x900')
    
    def leaveProg(self):
        sys.exit()