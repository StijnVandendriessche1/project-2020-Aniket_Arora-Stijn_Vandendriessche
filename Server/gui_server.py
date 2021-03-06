# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
import logging
import socket
from queue import Queue
from threading import Thread
from tkinter import *

from Server.gui_popular import ScreenPopular
from Server.server import SommenServer
from Server.gui_logged_on import ScreenLoggedOn
from Server.gui_client_data import ScreenClientData
from Server.gui_alert import ScreenAlert


class ServerWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.init_messages_queue()
        self.init_server()


    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Server")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Log-berichten Server:").grid(row=0)
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.lstnumbers = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lstnumbers.yview)

        self.lstnumbers.grid(row=1, column=0, sticky=N + S + E + W)
        self.scrollbar.grid(row=1, column=1, sticky=N + S)

        self.btn_text = StringVar()
        self.btn_text.set("Start Server")
        self.buttonServer = Button(self, textvariable=self.btn_text, command=self.start_stop_server)
        self.buttonServer.grid(row=3, column=0, columnspan=3, pady=(5, 5), padx=(5, 5), sticky=N + S + E + W)
        self.buttonServer = Button(self, text="alle clients", command=self.client_data)
        self.buttonServer.grid(row=4, column=0, pady=(5, 5), padx=(5, 5), sticky=N + S + E + W)
        self.buttonServer = Button(self, text="alert clients", command=self.alert)
        self.buttonServer.grid(row=5, column=0, pady=(5, 5), padx=(5, 5), sticky=N + S + E + W)
        self.buttonServer = Button(self, text="populair search queries", command=self.popular)
        self.buttonServer.grid(row=6, column=0, pady=(5, 5), padx=(5, 5), sticky=N + S + E + W)

        Grid.rowconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

    def init_server(self):
        # Server - init
        self.server = SommenServer(socket.gethostname(), 9999, self.messages_queue)

    def afsluiten_server(self):
        if self.server != None:
            self.server.close_server_socket()
        # del (self.messages_queue)

    def init_messages_queue(self):
        self.messages_queue = Queue()
        t = Thread(target=self.print_messsages_from_queue)
        t.start()

    def print_messsages_from_queue(self):
        message = self.messages_queue.get()
        while message != "CLOSE_SERVER":
            self.lstnumbers.insert(END, message)
            self.messages_queue.task_done()
            message = self.messages_queue.get()
        print("queue stop")

    def start_stop_server(self):
        if self.server.is_connected == True:
            if(self.btn_text.get() == "ingelogde clients"):
                t = ScreenLoggedOn(message_queue=self.messages_queue)
                t.start()
        else:
            self.server.init_server()
            self.server.start()             #thread!
            self.btn_text.set("ingelogde clients")

    def client_data(self):
        t = ScreenClientData(message_queue=self.messages_queue)
        t.start()

    def alert(self):
        try:
            t = ScreenAlert()
            t.start()
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)

    def popular(self):
        try:
            t = ScreenPopular()
            t.start()
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)
