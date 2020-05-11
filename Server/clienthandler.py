import math
import os
import threading
import pandas as pd
import random
import pickle
import json
import base64
import jsonpickle
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

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
        dd = self.data.drop('uuid', axis=1)
        dd = dd.drop('ord_in_thread', axis=1)
        dd = dd.drop('published', axis=1)
        dd = dd.drop('language', axis=1)
        dd = dd.drop('crawled', axis=1)
        dd = dd.drop('site_url', axis=1)
        dd = dd.drop('domain_rank', axis=1)
        dd = dd.drop('thread_title', axis=1)
        dd = dd.drop('spam_score', axis=1)
        dd = dd.drop('replies_count', axis=1)
        dd = dd.drop('participants_count', axis=1)
        dd = dd.drop('type', axis=1)
        dd = dd.dropna()
        dd.drop_duplicates(keep="first", inplace=True)
        dd.drop_duplicates("title", inplace=True)
        self.data = dd
        self.user = None

    def log_on(self, user):
        for i in ClientHandler.users:
            if i.email == user.email:
                return False
        self.user = user
        ClientHandler.users.append(self.user)
        if not self.exists_in_csv(user):
            self.write_user_to_csv()
        return True

    def exists_in_csv(self, user):
        u = pd.read_csv("../data/users.csv")
        return u['email'].str.contains(user.email).any()


    def write_user_to_csv(self):
        u = pd.read_csv("../data/users.csv")
        u = u.append({'name': self.user.name, 'nickname': self.user.nickname, 'email': self.user.email}, ignore_index=True)
        u.to_csv('../data/users.csv', index=False)


    def run(self):
        io_stream_client = self.socket_to_client.makefile(mode='rw')
        io_stream_client_bytes = self.socket_to_client.makefile(mode='rwb')
        self.print_bericht_gui_server("Waiting for numbers...")
        commando = io_stream_client.readline().rstrip('\n')
        while (commando != "CLOSE"):
            if commando == "login":
                answer = io_stream_client.readline().rstrip('\n')
                user = jsonpickle.decode(answer)
                a = self.log_on(user)
                if a:
                    io_stream_client.write("%s\n" % "success")
                    self.print_bericht_gui_server("%s logde zonet in als %s" % (self.user.name, self.user.nickname))
                else:
                    io_stream_client.write("%s\n" % "deze naam is momenteel al ingelogd")
                io_stream_client.flush()
            elif commando == "random":
                r = random.randint(0, 6411)
                a = Article(self.data.iloc[r].title, self.data.iloc[r].text,self.data.iloc[r].main_img_url, self.data.iloc[r].author, self.data.iloc[r].likes, self.data.iloc[r].shares, self.data.iloc[r].comments)
                x = jsonpickle.encode(a)
                io_stream_client.write("%s\n"%x)
                io_stream_client.flush()
            elif commando == "stats":
                dataset = pd.read_csv('../data/logboek.csv')
                dataset['hour'] = pd.DatetimeIndex(dataset['time']).strftime("%H")
                fig = plt.figure()
                sns.countplot(x='hour', data=dataset)
                pickle.dump(fig, io_stream_client_bytes)
            elif commando == "country":
                fig = plt.figure()
                sns.countplot(x='country', data=self.data)
                pickle.dump(fig, io_stream_client_bytes)
            elif commando == "author":
                fig = plt.figure()
                sns.countplot(x='author', data=self.data, order=self.data.author.value_counts().iloc[:5].index)
                pickle.dump(fig, io_stream_client_bytes)
            elif commando == "title":
                title = io_stream_client.readline().rstrip('\n')
                a = self.data.loc[self.data['title']==title]
                b = Article(a.title.values[0], a.text.values[0], a.main_img_url.values[0], a.author.values[0], a.likes.values[0], a.shares.values[0], a.comments.values[0])
                x = jsonpickle.encode(b)
                io_stream_client.write("%s\n" % x)
                io_stream_client.flush()
            elif commando == "top10":
                para = io_stream_client.readline().rstrip('\n')
                if para == "likes":
                    self.data = self.data.sort_values(by=['likes'], ascending=False)
                    a = []
                    for r in range(0,10):
                        b = Article(self.data.iloc[r].title, self.data.iloc[r].text,self.data.iloc[r].main_img_url, self.data.iloc[r].author, self.data.iloc[r].likes, self.data.iloc[r].shares, self.data.iloc[r].comments)
                        a.append(b)
                    x = jsonpickle.encode(a)
                    io_stream_client.write("%s\n" % x)
                    io_stream_client.flush()
                elif para == "comments":
                    self.data = self.data.sort_values(by=['comments'], ascending=False)
                    a = []
                    for r in range(0,10):
                        b = Article(self.data.iloc[r].title, self.data.iloc[r].text,self.data.iloc[r].main_img_url, self.data.iloc[r].author, self.data.iloc[r].likes, self.data.iloc[r].shares, self.data.iloc[r].comments)
                        a.append(b)
                    x = jsonpickle.encode(a)
                    io_stream_client.write("%s\n" % x)
                    io_stream_client.flush()
                elif para == "shares":
                    self.data = self.data.sort_values(by=['shares'], ascending=False)
                    a = []
                    for r in range(0,10):
                        b = Article(self.data.iloc[r].title, self.data.iloc[r].text,self.data.iloc[r].main_img_url, self.data.iloc[r].author, self.data.iloc[r].likes, self.data.iloc[r].shares, self.data.iloc[r].comments)
                        a.append(b)
                    x = jsonpickle.encode(a)
                    io_stream_client.write("%s\n" % x)
                    io_stream_client.flush()
            now = datetime.now()
            c = pd.read_csv("../data/logboek.csv")
            c = c.append({'user_mail': self.user.email, 'command': commando, 'time': now}, ignore_index=True)
            c.to_csv('../data/logboek.csv', index=False)
            commando = io_stream_client.readline().rstrip('\n')

        if self.user:
            self.print_bericht_gui_server("%s logde zonet uit (%s)" % (self.user.name, self.user.nickname))
            now = datetime.now()
            c = pd.read_csv("../data/logboek.csv")
            c = c.append({'user_mail': self.user.email, 'command': "logout", 'time': now}, ignore_index=True)
            c.to_csv('../data/logboek.csv', index=False)
            ClientHandler.users.remove(self.user)
        self.print_bericht_gui_server("Connection with client closed...")
        ClientHandler.numbers_clienthandlers -=1
        self.socket_to_client.close()

    def print_bericht_gui_server(self, message):
        self.messages_queue.put("CLH %d:> %s" % (self.id, message))

    def alert_message(self, message):
        io_stream_client = self.socket_to_client.makefile(mode='rw')
        io_stream_client.write("alert: %s\n" % message)
        io_stream_client.flush()