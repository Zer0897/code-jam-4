import configparser
import tkinter as tk
from contextlib import suppress

from .view import Window, View
from .front import Front
from .splash import Splash
from . import SETTINGS


parser = configparser.ConfigParser()
parser.read(SETTINGS)


class App(tk.Tk):
    appconfig = parser['APP']

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.resizable(False, False)
        for name, val in parser['APP'].items():
            getattr(self, name)(val)

        self.window = Window(self)
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
        self.execution_order = iter((
            self.splash,
            self.front,
            # self.result
        ))
        self.update()
        self.current: View = None
        self.after(0, self.switch)

    def switch(self):
        try:
            self.update()
            if self.current is not None:
                self.current.data.cleanup()
            self.current = next(self.execution_order)
            self.build(self.current)
        except StopIteration:
            self.cleanup()

    def build(self, view):
        self.update()
        view.master.change_view(view, 'up')
        self.update()
        view.data.build()

    def cleanup(self):
        with suppress(Exception):
            self.current.cleanup()
            self.destroy()
