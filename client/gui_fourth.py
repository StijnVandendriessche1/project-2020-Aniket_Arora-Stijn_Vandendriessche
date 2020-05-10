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


class Fourth(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Stats")
        self.master.geometry("640x480")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.get_img()

    def get_img(self):
        try:
            self.master.my_writer_obj.write("stats\n")
            # pickle.dump("stats", self.master.my_writer_obj)
            self.master.my_writer_obj.flush()
            answer = pickle.load(self.master.my_writer_obj_bytes)
            print(answer)

            fig_canvas = FigureCanvasTkAgg(answer, self.master)
            fig_canvas.draw()
            fig_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1.0)
            # answer = pickle.load(self.master.my_writer_obj)
            # number_of_sends = int(answer)
            # with open('received_file.png', 'wb+') as f:
            #     for i in range(0, number_of_sends):
            #         data = self.master.io_stream_client_bytes.read()
            #         f.write(data)
            # logging.info('Successfully get the image')

            # time.sleep(1)
            # im = Image.open('received_file.png')
            # self.img = ImageTk.PhotoImage(Image.open("received_file.png"))
            # self.lbl['image'] = self.img
            # # change size window
            # width, height = im.size
            # self.master.geometry("%dx%d" % (width, height))
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)