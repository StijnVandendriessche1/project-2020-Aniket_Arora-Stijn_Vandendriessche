import threading
import pandas as pd
class ClientHandler(threading.Thread):

    numbers_clienthandlers = 0

    def __init__(self, socketclient, messages_queue):
        threading.Thread.__init__(self)
        #connectie with client
        self.socket_to_client = socketclient
        #message queue -> link to gui Server
        self.messages_queue = messages_queue
        #id clienthandler
        self.id = ClientHandler.numbers_clienthandlers
        ClientHandler.numbers_clienthandlers += 1


    def run(self):
        io_stream_client = self.socket_to_client.makefile(mode='rw')

        self.print_bericht_gui_server("Waiting for numbers...")
        commando = io_stream_client.readline().rstrip('\n')
        while (commando != "CLOSE"):
            if commando == "login":
                naam = io_stream_client.readline().rstrip('\n')
                users = pd.read_csv('../data/users.csv')
                a = users['naam'].where(users['naam'] == naam)
                print(a)
                if(a.dropna().empty):
                    record = pd.DataFrame([[naam]], columns=["naam"])
                    users = pd.concat([record, users], ignore_index=True)
                    users.to_csv('../data/users.csv', index=False)
                    self.print_bericht_gui_server(naam + " was logged in")
                    io_stream_client.write("%s\n" % "ingelogd")
                else:
                    io_stream_client.write("%s\n" % "deze naam is momenteel al ingelogd")
            io_stream_client.flush()

            commando = io_stream_client.readline().rstrip('\n')

        self.print_bericht_gui_server("Connection with client closed...")
        self.socket_to_client.close()

    def print_bericht_gui_server(self, message):
        self.messages_queue.put("CLH %d:> %s" % (self.id, message))
