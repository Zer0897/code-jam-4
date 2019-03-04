import json

from .view import Window, View
from .animate import Direction, BounceBall, Direction
from . import widget, DOCS


class Splash(widget.PrimaryFrame):

    with (DOCS / 'questions.json').open() as fp:
        questions = json.load(fp)

    def init(self):
        self.intro = Intro(self, bg='gray')

        self.btn_confirm = widget.PrimaryButton(
            self.intro.window, command=self.switch, text='Okay'
        )
        self.bounce(
            View(self.intro.window, window=self.btn_confirm)
        )
        self.intro.pack(fill='both', expand=True)
        self.after(0, self.intro.build)

    def bounce(self, view):
        self.update()
        wid = self.intro.window.set_view(view, (Direction.RIGHT * 100) + (Direction.DOWN * 100))
        motion = BounceBall(view.master, wid, view.master.origin, speed=6)
        view.master.animater.add(motion)
        motion.kick(Direction.UP + Direction.LEFT)
        self.update()
        self.after(0, view.master.animater.start)

    def switch(self):
        self.master.switch()

    def cleanup(self):
        self.intro.cleanup()


class Intro(widget.PrimaryFrame):
    intro = (DOCS / 'intro.txt').read_text()

    def init(self):
        self.window = Window(self)
        width = 400
        self.title = widget.PrimaryLabel(
            self,
            text=self.master.master.title(),  # yikes
            font=('Courier', 14),
            wraplength=width, justify='center', fg='blue',

        )
        self.title.pack(fill='both', expand=True)
        self.window.pack(fill='both', expand=True)
        self.update()
        self.intro = View(
            self.window,
            text=self.intro,
            width=width,
            font=('sys', 12), justify='center',
            fill='red'
        )

    def build(self):
        self.after(0, self.window.set_view, self.intro)
        self.update()

    def cleanup(self):
        self.window.animater.clear()


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
