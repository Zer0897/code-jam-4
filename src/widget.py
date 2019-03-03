import tkinter as tk
from configparser import ConfigParser
from . import THEME, IMAGES

parser = ConfigParser()
parser.read(THEME)

primary = parser['primary']
secondary = parser['secondary']
base = parser['base']


class SecondaryFrame(tk.Frame):
    DEFAULT = {
        **base, **secondary,
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class SecondaryButton(tk.Button):
    DEFAULT = {
        **base, **secondary,
        'height': 1,
        'width': 10
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class SecondaryLabel(tk.Label):
    DEFAULT = {
        **base, **secondary,
        'justify': 'left',
        'width': 10,
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class SecondaryCanvas(tk.Canvas):
    DEFAULT = {
        **base, **secondary,
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class PrimaryFrame(tk.Frame):
    DEFAULT = {
        **base, **primary
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class PrimaryButton(tk.Button):
    DEFAULT = {
        **base, **primary,
        'height': 3, 'width': 10
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class PrimaryLabel(tk.Label):
    DEFAULT = {
        **base, **primary,
        'font': ('Courier', 25),
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class PrimaryCanvas(tk.Canvas):
    DEFAULT = {
        **base, **primary,
    }

    def __init__(self, *args, **kwds):
        super().__init__(*args, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()


class PrimaryCheckbutton(tk.Checkbutton):
    DEFAULT = {
        **base, **primary,
    }
    img = IMAGES / 'checkbox.png'

    def __init__(self, *args, **kwds):
        img = tk.PhotoImage(file=self.img)
        super().__init__(*args, image=img, **{**self.DEFAULT, **kwds})
        if hasattr(self, 'init'):
            self.init()
