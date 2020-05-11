import logging
import pickle
import socket
import time
from tkinter import *
from tkinter import messagebox
import jsonpickle
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from domein.user import User


class ServerStats(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Server Stats")
        self.master.geometry("640x540")
        self.get_img()

    def get_img(self):
        try:
            lbl = Label(self.master, text="Activiteit per uur:")
            lbl.grid(column=0, row=0, columnspan=2)
            self.master.my_writer_obj.write("stats\n")
            self.master.my_writer_obj.flush()
            answer = pickle.load(self.master.my_writer_obj_bytes)
            print(answer)

            fig_canvas = FigureCanvasTkAgg(answer, master=self.master)
            fig_canvas.draw()
            fig_canvas.get_tk_widget().grid(row=1, column=0)
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)

    def back(self):
        self.master.switch_frame("stats")