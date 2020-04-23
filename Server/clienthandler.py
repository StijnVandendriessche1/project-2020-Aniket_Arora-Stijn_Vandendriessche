import threading
import pandas as pd
import random
import pickle
import json
import base64
import jsonpickle

from domein.article import Article

class ClientHandler(threading.Thread):

    numbers_clienthandlers = 0
    users = []

    def __init__(self, socketclient, messages_queue):
        threading.Thread.__init__(self)
        #connectie with client
        self.socket_to_client = socketclient
        #message queue -> link to gui Server
        self.messages_queue = messages_queue
        #id clienthandler
        self.id = ClientHandler.numbers_clienthandlers
        ClientHandler.numbers_clienthandlers += 1
        self.data = pd.read_csv("../data/fake.csv")

    def log_on(self, name):
        for i in ClientHandler.users:
            if name == i:
                return False
        self.name = name
        ClientHandler.users.append(name)
        return True


    def run(self):
        io_stream_client = self.socket_to_client.makefile(mode='rw')
        naam = ""
        self.print_bericht_gui_server("Waiting for numbers...")
        commando = io_stream_client.readline().rstrip('\n')
        while (commando != "CLOSE"):
            if commando == "login":
                naam = io_stream_client.readline().rstrip('\n')
                a = self.log_on(naam)
                if a:
                    io_stream_client.write("%s\n" % "success")
                    self.messages_queue.put("´s logde zonet in" % naam)
                else:
                    io_stream_client.write("%s\n" % "deze naam is momenteel al ingelogd")
                io_stream_client.flush()
            elif commando == "random":
                r = random.randint(0, 12999)
                a = Article(self.data.iloc[r].title, self.data.iloc[r].text,self.data.iloc[r].main_img_url)
                x = jsonpickle.encode(a)
                io_stream_client.write("%s\n"%x)
                io_stream_client.flush()
            commando = io_stream_client.readline().rstrip('\n')

        users = pd.read_csv('../data/users.csv')
        users = users[users.naam != naam]
        users.to_csv('../data/users.csv', index=False)
        self.print_bericht_gui_server("Connection with client closed...")
        self.socket_to_client.close()

    def print_bericht_gui_server(self, message):
        self.messages_queue.put("CLH %d:> %s" % (self.id, message))
