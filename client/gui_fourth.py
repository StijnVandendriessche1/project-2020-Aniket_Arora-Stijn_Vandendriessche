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


class Fourth(Frame):
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
        self.master.title("Land")
        self.master.geometry("175x130")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)