# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
import logging
import socket
from tkinter import *
from tkinter import messagebox
import jsonpickle
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd
from domein.user import User


class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        # Variables
        self.user = None

        self.dataset_users = pd.read_csv('../data/users.csv')

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Registreren")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Naam:").grid(row=0)
        self.entry_naam = Entry(self, width=40)
        Label(self, text="Nickname:").grid(row=1)
        self.entry_nickname = Entry(self, width=40)
        Label(self, text="Email:").grid(row=2)
        self.entry_email = Entry(self, width=40)

        self.entry_naam.grid(row=0, column=1, sticky=E + W, padx=(5, 5), pady =(5,5))
        self.entry_nickname.grid(row=1, column=1, sticky=E + W, padx=(5, 5), pady=(5, 5))
        self.entry_email.grid(row=2, column=1, sticky=E + W, padx=(5, 5), pady=(5, 5))

        self.label_resultaat = Label(self, width=40, anchor='w')
        self.label_resultaat.grid(row=3, column=1, sticky=E + W)

        self.btnRegister = Button(self, text="Log in", command=self.login)
        self.btnRegister.grid(row=4, column=0, columnspan=2, pady=(0, 5), padx=(5, 5), sticky=N + S + E + W)

        Grid.rowconfigure(self, 5, weight=1)
        Grid.columnconfigure(self, 1, weight=1)

    def login(self):
        try:
            self.user = User(self.entry_naam.get(), self.entry_nickname.get(), self.entry_email.get())
            self.master.my_writer_obj.write("login\n")
            x = jsonpickle.encode(self.user)
            self.master.my_writer_obj.write("%s\n" % x)
            self.master.my_writer_obj.flush()

            # # waiting for answer

            answer = self.master.my_writer_obj.readline().rstrip('\n')
            logging.info("Answer server: %s" % answer)
            self.label_resultaat['text'] = answer
            if answer == "success":
                logging.info(answer)
                self.master.switch_frame("dashboard")
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)
            messagebox.showinfo("Log in", "Something has gone wrong...")
