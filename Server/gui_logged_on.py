import threading
import pandas as pd
from tkinter import *
from tkinter import scrolledtext
from Server.clienthandler import ClientHandler
import time
from Server.server import SommenServer

class ScreenLoggedOn(threading.Thread):

    numbers_clienthandlers = 0

    def __init__(self, message_queue):
        threading.Thread.__init__(self)
        self.init_window()
        self.messages_queue = message_queue

    def init_window(self):
        self.window = Tk()
        self.window.title("ingelogde clients")
        self.window.geometry('350x200')
        lbl = Label(self.window, text="Momenteel zijn volgende clients ingelogd:")
        lbl.grid(column=0, row=0)
        self.txt = scrolledtext.ScrolledText(self.window, width=40, height=10)
        self.txt.grid(column=0, columnspan=2, row=1)
        self.users = ClientHandler.users
        for us in self.users:
            self.txt.insert(INSERT, us + "\n")
        t = threading.Thread(target=self.update)
        t.start()
        self.window.mainloop()

    def update(self):
        while True:
            self.txt.delete('1.0', END)
            for us in ClientHandler.users:
                self.txt.insert(INSERT, us + "\n")
            time.sleep(0.5)

    def print_bericht_gui_server(self, message):
        self.messages_queue.put("CLH %d:> %s" % (self.id, message))