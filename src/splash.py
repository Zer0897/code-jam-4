import json

from .view import Window, View
from .animate import Direction, BounceBall
from . import widget, DOCS


class Splash(widget.PrimaryFrame):

    with (DOCS / 'questions.json').open() as fp:
        questions = json.load(fp)

    def init(self):
        self.intro = Intro(self)
        self.intro.pack(fill='both', expand=True)

        self.btn_confirm = widget.PrimaryButton(self.intro.window, command=self.next, text='Okay')

    def build(self):
        self.intro.build()
        bouncer = View(self.intro.window, window=self.btn_confirm)
        self.bounce(bouncer)

    def bounce(self, view):
        start = view.master.center + (Direction.LEFT * 175) + (Direction.DOWN * 100)
        wid = view.master.set_view(view, start)
        motion = BounceBall(view.master, wid, view.master.origin, speed=6)
        motion.kick(Direction.UP)
        self.after(0, view.master.run, motion)

    def next(self):
        self.master.master.switch()


class Intro(widget.PrimaryFrame):
    intro = (DOCS / 'intro.txt').read_text()

    def init(self):
        self.window = Window(self, bg='gray')
        self.window.pack(fill='both', expand=True)
        self.update()

        width = self.winfo_reqwidth()
        self.title = View(
            self.window,
            text=self.master.master.master.title(),  # yikes
            font=('Courier', 17),
            width=width, justify='center'
        )
        self.intro = View(
            self.window,
            text=self.intro,
            width=width,
            font=('sys', 12), justify='center'
        )
        self.update()

    def build(self):
        self.window.set_view(self.title)
        adjust = (Direction.LEFT * 175) + (Direction.DOWN * 100)
        self.window.set_view(
            self.intro,
            self.window.center + adjust
        )


class Question(widget.PrimaryFrame):

    def init(self):
        self.title = widget.PrimaryLabel(self)
        self.choices = widget.SecondaryFrame(self)

        self.options = []

    def load(self, choices):
        for question in questions:
            frame = widget.SecondaryFrame(self.choices)
            check = widget.PrimaryCheckbutton(frame)
            val = widget.SecondaryLabel(frame, text=question)

            frame.pack()
            check.pack(side='left')
            val.pack(side='left')

        self.title.pack(fill='both', expand=True)
        self.choices.pack(fill='both', expand=True)
