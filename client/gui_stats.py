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


class Stats(Frame):
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
        self.master.title("Statistieken")
        self.master.geometry("175x130")
        # allowing the widget to take the full space of the root window
        # self.pack(fill=BOTH, expand=1)

        self.btnTop10 = Button(self, text="Top 10", command=self.top10)
        self.btnTop10.grid(row=1, padx=(16, 16), pady=(16, 16), sticky=N + S + E + W)
        self.btnAuthor = Button(self, text="Auteur", command=self.auteur)
        self.btnAuthor.grid(row=1,column=1, pady=(16, 16), sticky=N + S + E + W)
        self.btnCountry = Button(self, text="Land", command=self.country)
        self.btnCountry.grid(row=2, padx=(16, 16), sticky=N + S + E + W)
        self.btnSomething = Button(self, text="Server stats", command=self.fourth)
        self.btnSomething.grid(row=2,column=1, sticky=N + S + E + W)
        self.btnBack = Button(self, text="Terug", command=self.back)
        self.btnBack.grid(row=3, columnspan=2, padx=(16, 16), pady=(16, 16), sticky=N + S + E + W)

    def fourth(self):
        self.master.switch_frame("fourth")

    def back(self):
        self.master.switch_frame("dashboard")

    def top10(self):
        self.master.switch_frame("top10")

    def auteur(self):
        self.master.switch_frame("auteur")

    def country(self):
        self.master.switch_frame("country")