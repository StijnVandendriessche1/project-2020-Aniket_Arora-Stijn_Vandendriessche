import threading
import pandas as pd
import seaborn as sns
from tkinter import *
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import logging
from tkinter import scrolledtext
from Server.clienthandler import ClientHandler
import time
from Server.server import SommenServer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ScreenPopular(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.init_window()

    def init_window(self):
        try:
            self.window = Tk()
            self.window.title("Popular")
            self.window.geometry('640x500')
            lbl = Label(self.window, text="Meest populaire zoekopdrachten:")
            lbl.grid(column=0, row=0, columnspan=2)

            fig = plt.figure()
            dataset = pd.read_csv('../data/logboek.csv')
            sns.countplot(x='command', data=dataset)
            fig_canvas = FigureCanvasTkAgg(fig, master=self.window)
            fig_canvas.draw()
            fig_canvas.get_tk_widget().grid(row=1, column=0)
            print(fig)
        except Exception as ex:
            logging.error(ex)
