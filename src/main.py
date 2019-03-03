import configparser
import tkinter as tk
from contextlib import suppress

from .view import Window, View
from .front import Front
from .splash import Splash
from . import SETTINGS, widget


parser = configparser.ConfigParser()
parser.read(SETTINGS)


class App(tk.Tk):
    appconfig = parser['APP']

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.resizable(False, False)
        for name, val in parser['APP'].items():
            getattr(self, name)(val)

        # self.frame = widget.PrimaryFrame(self)
        self.window = Window(self)

        # self.frame.pack(expand=True, fill='both')
        self.window.pack(expand=True, fill='both')

        self.update()
        self.splash = View(
            self.window,
            window=Splash(self.window),
            height=self.winfo_height(),
            width=self.winfo_width()
        )
        self.front = View(
            self.window,
            window=Front(self.window),
            height=self.winfo_height(),
            width=self.winfo_width()
        )
        self.after(0, self.build, self.splash)

    def build(self, view):
        self.update()
        view.master.set_view(view)
        view.data.build()

    def cleanup(self):
        with suppress(Exception):
            self.front.cleanup()
            self.destroy()
