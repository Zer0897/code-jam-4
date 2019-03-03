import configparser
import tkinter as tk
from contextlib import suppress

from .front import Front
from .splash import Splash
from . import SETTINGS


parser = configparser.ConfigParser()
parser.read(SETTINGS)


class App(tk.Tk):
    appconfig = parser['APP']

    def __init__(self, *args, **kwds):
        title = self.appconfig.pop('title')
        super().__init__(*args, **kwds)
        self.title = title

        self.geometry = '400x500'
        self.minsize(400, 500)
        self.maxsize(400, 500)

        self.splash = Splash(self)
        self.splash.pack(expand=True, fill='both')
        # self.front = Front(self)
        # self.front.pack(fill='both', expand=True)

    def cleanup(self):
        with suppress(Exception):
            self.front.cleanup()
            self.destroy()
