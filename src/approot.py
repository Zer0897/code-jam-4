import tkinter as tk
import time


class AppRoot(tk.Tk):
    def __init__(self, *args, **kwargs):
        # init the root
        tk.Tk.__init__(self, *args, **kwargs)

        # make a Canvas
        self.container = tk.Canvas(self, width=400, height=500, bg="black")

        # set frames dict
        self.frames = dict()

    def show_frame(self, page_name):
        '''Show a frame for the given page name (Animates the BioPage 
        to either slide up or down'''
        try:
            # get the Bio Page id
            frame = self.frames["BioPage"]
        except:
            # it doesn't exist, do nothing
            return
        def animate():
            '''Animates the bio page sliding up'''
            if page_name == "MainPage":
                # move the frame down 2 pixels 250 times
                for i in range(250):
                    self.container.move(frame, 0, 2)
                    self.container.update()
            else:
                # move the frame up 2 pixels 250 times
                for i in range(250):
                    self.container.move(frame, 0, -2)
                    self.container.update()
        # after 0 seconds, run animate (this makes it not blocking)
        self.after(0, animate)

    def add_page(self, page, page_name):
        '''Adds a page to the canvas with the given name'''
        # if it's a bio page, make it lower so we can scroll it up
        if name == "BioPage":
            frame_id = self.container.create_window(200, 750, window=page)
        else:
            frame_id = self.container.create_window(200, 250, window=page)
        # pack the container
        self.container.pack()
        # add the frame id to the frames dict
        self.frames[name] = frame_id
