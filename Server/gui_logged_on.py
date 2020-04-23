import threading
import pandas as pd
from tkinter import *
from tkinter import scrolledtext

class ScreenLoggedOn(threading.Thread):

    numbers_clienthandlers = 0

    def __init__(self, message_queue):
        threading.Thread.__init__(self)
        self.init_window()
        self.message_queue = message_queue

    def init_window(self):
        self.window = Tk()
        self.window.title("ingelogde clients")
        self.window.geometry('350x200')
        lbl = Label(self.window, text="Momenteel zijn volgende clients ingelogd:")
        lbl.grid(column=0, row=0)
        txt = scrolledtext.ScrolledText(self.window, width=40, height=10)
        txt.grid(column=0, columnspan=2, row=1)
        users = pd.read_csv('../data/users.csv')
        u = users.naam
        for us in u:
            txt.insert(INSERT, us + "\n")
        self.window.mainloop()