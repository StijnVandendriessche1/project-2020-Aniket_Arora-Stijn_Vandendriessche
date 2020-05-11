import threading
import pandas as pd
from tkinter import *
from tkinter import scrolledtext
from Server.clienthandler import ClientHandler
import time
from Server.server import SommenServer

class ScreenClientData(threading.Thread):

    def __init__(self, message_queue):
        threading.Thread.__init__(self)
        self.init_window()
        self.messages_queue = message_queue

    def init_window(self):
        self.window = Tk()
        self.window.title("clients")
        self.window.geometry('500x300')
        lbl = Label(self.window, text="Alle clients die in het systeem zijn opgenomen:")
        lbl.grid(column=0, row=0, columnspan=2)
        self.txt = scrolledtext.ScrolledText(self.window, width=60, height=17)
        self.txt.grid(column=0, columnspan=2, row=1)
        us = pd.read_csv("../data/users.csv")
        print(us.shape)

        for ind in us.index:
            self.txt.insert(INSERT, "name: %s\nnickname: %s\nemail: %s\n\n" % (us['name'][ind], us['nickname'][ind], us['email'][ind]))
        self.window.mainloop()

    def print_bericht_gui_server(self, message):
        self.messages_queue.put("CLH %d:> %s" % (self.id, message))