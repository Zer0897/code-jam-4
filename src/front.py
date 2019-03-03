import io
from PIL import Image, ImageTk

from . import widget
from .animate import Direction
from .view import Window, View
from .cache import ImageCache
from .loading import Loading
from .quiz import Quiz

def process_image(image: bytes, width: int, height: int):
    im = Image.open(io.BytesIO(image))
    im = im.resize((width, height), Image.NEAREST)
    return ImageTk.PhotoImage(im)


class Front(widget.PrimaryFrame):

    cachesize = 20
    quiz = Quiz()

    # Quick fix to keep a reference count on the
    # last image, making sure the garbage collector
    # doesn't delete it before the animation ends
    _last = None

    def __next(self, direction: Direction = None):
        data: dict = self.cache.next()
        image = process_image(
            data.pop('image'),
            self.window.winfo_width(),
            self.window.winfo_height()
        )
        name = data.pop('name')
        self.__load(name, image, data)
        if direction is None:
            self.window.set_view(self.image)
        else:
            self.window.change_view(self.image, direction)

    def __load(self, name, image, data):
        self.title.config(text=name)
        self.image = View(image, 'image')
        self.bio = View(Bio(self.window), 'widget')

        self._last = self.image
        self.bio.data.load(data)
        self.update()

    def init(self):
        self.title = widget.PrimaryLabel(self)
        self.window = Window(self)
        self.commandbar = widget.SecondaryFrame(self)

        self.bio = None
        self.image = None

        self.btn_dislike = widget.PrimaryButton(
            self.commandbar, text='Nope', bg='red', command=self.cmd_dislike
        )
        self.btn_bio = widget.SecondaryButton(
            self.commandbar, text='Bio', command=self.cmd_bio
        )
        self.btn_like = widget.PrimaryButton(
            self.commandbar, text='Yep', bg='green', command=self.cmd_like
        )
        self.title.pack(fill='x', expand=True)
        self.window.pack(fill='both', expand=True)
        self.commandbar.pack(side='bottom', fill='both', expand=True)

        self.btn_dislike.pack(side='left')
        self.btn_like.pack(side='right')
        self.btn_bio.pack()

        self.cache = ImageCache(self.cachesize)
        self.cache.start()
        self.after(0, self.__next)

    def cmd_dislike(self):
        self.quiz.dislikes+=1
        self.__next('left')

    def cmd_like(self):
        self.quiz.likes+=1
        self.__next('right')

    def cmd_bio(self):
        if self.window.current != self.bio:
            self.window.change_view(self.bio, 'up')
        else:
            self.window.change_view(self.image, 'down')

    def cleanup(self):
        self.cache.stop()


class Bio(widget.PrimaryFrame):

    def init(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        self.config(height=height, width=width)
        self.pack_propagate(0)

    def __build_info(self, info: dict):
        item = widget.PrimaryFrame(self)
        info = [
            f"Age: {info['age']}",
            info['gender'].capitalize(),
            f'{"She" if info["gender"].startswith("f") else "He"} is {info["location"]}.'
        ]
        for val in info:
            name = widget.PrimaryLabel(item, text=val, font=('sys', 15), fg='gray')
            name.pack(fill='both')
        return item

    def __build_hobbies(self, hobbies):
        frame = widget.PrimaryFrame(self)
        title = widget.PrimaryLabel(frame, text='Hobbies', font=('sys', 15), justify='left')
        title.pack(fill='both')
        for hobby in hobbies:
            val = widget.SecondaryLabel(frame, text=hobby)
            val.pack(fill='both')
        return frame

    def load(self, data: dict):
        info = self.__build_info(data['info'])
        hobbies = self.__build_hobbies(data['hobbies'])
        info.pack(expand=True, fill='both')
        hobbies.pack(expand=True, fill='both')


class Splash(widget.PrimaryFrame):

    def init(self):
        self.window = Window(self)

