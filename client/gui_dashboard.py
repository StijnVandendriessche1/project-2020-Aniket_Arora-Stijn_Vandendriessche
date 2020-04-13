import logging
import socket
from tkinter import *
from tkinter import messagebox


class Dashboard(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        #self.my_writer_obj = writer

    # Creation of init_window
    def init_window(self):
        self.master.title("Dashboard")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="Dashboard").grid(row=0)

        self.btn_text = StringVar()
        self.btn_text.set("Get random fake-news article")
        self.buttonServer = Button(self, textvariable=self.btn_text, command=self.getRandom)
        self.buttonServer.grid(row=3, column=0, columnspan=3, pady=(5, 5), padx=(5, 5), sticky=N + S + E + W)

    def __del__(self):
        self.close_connection()

    def getRandom(self):
        self.my_writer_obj.write("random\n")
        self.my_writer_obj.flush()
        answer = self.my_writer_obj.readline().rstrip('\n')
        print(answer)