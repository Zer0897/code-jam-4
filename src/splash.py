import json

from .view import Window, View
from .animate import Direction, BounceBall
from . import widget, DOCS


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


class Splash(widget.PrimaryFrame):

    intro = (DOCS / 'intro.txt').read_text()
    with (DOCS / 'questions.json').open() as fp:
        questions = json.load(fp)

    def init(self):
        self.window = Window(self, bg='gray')
        self.title = widget.PrimaryLabel(
            self, text=self.master.master.title(),
            font=('Courier', 17), wraplength=300
        )
        self.intro = View(
            self.window,
            text=self.intro,
            width=self.window.winfo_reqwidth(),
            font=('sys', 12), justify='center'
        )
        self.window.set_view(self.intro)

        self.btn_confirm = widget.PrimaryButton(self.window, command=self.begin, text='Okay')

        self.title.pack(fill='both')
        self.window.pack(fill='both')
        self.bounce()

    def bounce(self):
        bouncer = View(self.window, window=self.btn_confirm)
        wid = self.window.set_view(bouncer, self.window.center)
        motion = BounceBall(self.window, wid, self.window.origin, speed=6)
        motion.kick(Direction.DOWN)
        self.after(0, self.window.run, motion)

    def begin(self):
        pass
