import threading
import pandas as pd
import seaborn as sns
from tkinter import *
from PIL import Image, ImageTk
import logging
from tkinter import scrolledtext
from Server.clienthandler import ClientHandler
import time
from Server.server import SommenServer


class ScreenAlert(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.init_window()

    def init_window(self):
        self.window = Tk()
        self.window.title("Alert")
        self.window.geometry('500x300')

        self.entSearch = Entry(self.window, width=32, font=("arial", 16), foreground="gray")
        self.entSearch.grid(row=1, column=1, sticky=E + W, pady=(32, 32), padx=(16, 16))

        self.btnSearch = Button(self.window, text="Stuur Alert!", command=self.send_alert)
        self.btnSearch.grid(row=1, column=2, pady=(32, 32), sticky=N + S + E + W)

    def send_alert(self):
        message = self.entSearch.get()
        try: 
            for client in SommenServer.clients:
                try:
                    client.alert_message(message)
                except Exception as ex:
                    logging.error("Client not found")
        except Exception as ex:
            logging.error(ex)
