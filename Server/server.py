import logging
import socket
import threading
import pandas as pd

from Server.clienthandler import ClientHandler

logging.basicConfig(level=logging.INFO)

class SommenServer(threading.Thread):
    clients = []

    def __init__(self, host, port, messages_queue):
        threading.Thread.__init__(self)
        self.__is_connected = False
        self.host = host
        self.port = port
        # self.init_server(host, port)                #Server niet onmiddellijk initialiseren (via GUI)
        self.messages_queue = messages_queue

    @property
    def is_connected(self):
        return self.__is_connected


    def init_server(self):
        # create a socket object
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((self.host, self.port))
        self.serversocket.listen(5)
        self.__is_connected = True
        self.print_bericht_gui_server("SERVER STARTED")


    def close_server_socket(self):
        self.print_bericht_gui_server("CLOSE_SERVER")
        self.serversocket.close()


    # thread-klasse!
    def run(self):
        number_received_message = 0
        try:
            while True:
                self.print_bericht_gui_server("waiting for a new client...")

                # establish a connection
                socket_to_client, addr = self.serversocket.accept()
                self.print_bericht_gui_server("Got a connection from %s" % str(addr))
                clh = ClientHandler(socket_to_client, self.messages_queue)
                clh.start()
                self.print_bericht_gui_server("Current Thread count: %i." % threading.active_count())
                SommenServer.clients.append(clh)

        except Exception as ex:
            self.print_bericht_gui_server("Serversocket afgesloten")


    def print_bericht_gui_server(self, message):
        self.messages_queue.put("Server:> %s" %message)