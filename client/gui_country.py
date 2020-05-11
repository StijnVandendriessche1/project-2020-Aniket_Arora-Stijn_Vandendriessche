import logging
import pickle
import socket
from tkinter import *
from tkinter import messagebox
import jsonpickle
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from domein.user import User


class Country(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Land")
        self.master.geometry("640x480")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.get_img()

    def get_img(self):
        try:
            self.master.my_writer_obj.write("country\n")
            self.master.my_writer_obj.flush()
            answer = pickle.load(self.master.my_writer_obj_bytes)
            print(answer)

            fig_canvas = FigureCanvasTkAgg(answer, self.master)
            fig_canvas.draw()
            fig_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1.0)
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)