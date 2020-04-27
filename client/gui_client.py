# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
import logging
import socket
from tkinter import *
from tkinter import messagebox
import jsonpickle
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd


class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        # Variables
        self.name = ""
        self.nickname = ""
        self.email = ""

        self.dataset_users = pd.read_csv('data/users.csv')

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Registreren")
        self.master.geometry("400x300")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Naam:").grid(row=0)

        self.entry_naam = Entry(self, width=40)
        self.label_resultaat = Label(self, width=40, anchor='w'  )

        self.entry_naam.grid(row=0, column=1, sticky=E + W, padx=(5, 5), pady =(5,5))
        self.label_resultaat.grid(row=2, column=1, sticky=E + W)

        self.btnRegister = Button(self, text="Log in", command=self.login)
        self.btnRegister.grid(row=3, column=0, columnspan=2, pady=(0, 5), padx=(5, 5), sticky=N + S + E + W)

        Grid.rowconfigure(self, 3, weight=1)
        Grid.columnconfigure(self, 1, weight=1)

    def login(self):
        try:
            naam = self.entry_naam.get()
            self.master.my_writer_obj.write("login\n")
            self.master.my_writer_obj.write("%s\n" % naam)
            self.master.my_writer_obj.flush()

            # # waiting for answer

            answer = self.master.my_writer_obj.readline().rstrip('\n')
            logging.info("Answer server: %s" % answer)
            self.label_resultaat['text'] = answer
            if answer == "success":
                logging.info(answer)
                self.master.switch_frame("dashboard")
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)
            messagebox.showinfo("Sommen", "Something has gone wrong...")

    def get_random(self):
        self.master.my_writer_obj.write("random\n")
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        print(art.title)

    def get_by_title(self, title="Mikhail Saakashvili quits as Odessa governor"):
        self.master.geometry("1280x720")
        self.my_writer_obj.write("title\n")
        self.my_writer_obj.write("%s\n" % title)
        self.my_writer_obj.flush()
        answer = self.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        print(art.img)

        self.label_title(self, text=title)

        #sample code van img in tkinter
        #resp = requests.get(art.img)
        #load = Image.open(BytesIO(resp.content))
        #render = ImageTk.PhotoImage(load)
        #img = Label(image=render)
        #img.image = render
        #img.place(x=0,y=0)

    def append_user_csv(self):
        dataframe_user = pd.DataFrame({"name": [self.name],
                                       "nickname": [self.nickname],
                                       "email": [self.email]})
        logging.info('Made user')
        pd.concat([self.dataset_users, dataframe_user], axis=0, ignore_index=True)
        self.dataset_users.to_csv('data/users.csv', index=False)
        logging.info('Appending users.csv with new dataset')
