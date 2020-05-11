import logging
import socket
from tkinter import *
from tkinter import messagebox
import jsonpickle
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd
from domein.user import User


class Top10(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.options = ["likes", "comments", "shares"]
        self.dropdownSelected = StringVar()
        self.dropdownSelected.set(self.options[0])
        self.dropdownSelected.trace("w", self.changeDropDown)
        self.FirstTitel = StringVar()
        self.FirstLikes = StringVar()
        self.SecondTitel = StringVar()
        self.ThirdTitel = StringVar()
        self.FourthTitel = StringVar()
        self.FifthTitel = StringVar()
        self.SixthTitel = StringVar()
        self.SeventhTitel = StringVar()
        self.EighthTitel = StringVar()
        self.NinethTitel = StringVar()
        self.TenthTitel = StringVar()
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Top 10")
        self.master.geometry("960x750")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.Title = Label(self, text="Top 10", font=("Arial", 24, "bold italic")).grid(row=1, column=1, columnspan=4)

        self.DDMenu = OptionMenu(self, self.dropdownSelected, *self.options)
        self.DDMenu.grid(row=2, padx=(16, 16), pady=(16, 16), sticky=N + S + E + W, columnspan=4)

        self.First = Label(self, textvariable=self.FirstTitel, font=("Arial", 12)).grid(row=3, column=1)

        self.Second = Label(self, textvariable=self.SecondTitel, font=("Arial", 12)).grid(row=4, column=1)

        self.Third = Label(self, textvariable=self.ThirdTitel, font=("Arial", 12)).grid(row=5, column=1)

        self.Fourth = Label(self, textvariable=self.FourthTitel, font=("Arial", 12)).grid(row=6, column=1)

        self.Fifth = Label(self, textvariable=self.FifthTitel, font=("Arial", 12)).grid(row=7, column=1)

        self.Sixth = Label(self, textvariable=self.SixthTitel, font=("Arial", 12)).grid(row=8, column=1)

        self.Seventh = Label(self, textvariable=self.SeventhTitel, font=("Arial", 12)).grid(row=9, column=1)

        self.Eighth = Label(self, textvariable=self.EighthTitel, font=("Arial", 12)).grid(row=10, column=1)

        self.Nineth = Label(self, textvariable=self.NinethTitel, font=("Arial", 12)).grid(row=11, column=1)

        self.Tenth = Label(self, textvariable=self.TenthTitel, font=("Arial", 12)).grid(row=12, column=1)

        self.btnBack = Button(self, text="Terug", command=self.back)
        self.btnBack.grid(row=13, columnspan=2, padx=(16, 16), pady=(16, 16), sticky=N + S + E + W)

        self.get_top10()

    def changeDropDown(self, *args):
        self.get_top10(self.dropdownSelected.get())

    def get_top10(self, par="likes"):
        self.master.my_writer_obj.write("top10\n")
        self.master.my_writer_obj.write("%s\n"%par)
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        self.FirstTitel.set("1 - " + art[0].title + "\nLikes: " + str(art[0].likes) + "   Comments: " + str(art[0].comments) + "   Shares: " + str(art[0].shares) + "\n")
        self.SecondTitel.set("2 - " + art[1].title + "\nLikes: " + str(art[1].likes) + "   Comments: " + str(art[1].comments) + "   Shares: " + str(art[1].shares) + "\n")
        self.ThirdTitel.set("3 - " + art[2].title + "\nLikes: " + str(art[2].likes) + "   Comments: " + str(art[2].comments) + "   Shares: " + str(art[2].shares) + "\n")
        self.FourthTitel.set("4 - " + art[3].title + "\nLikes: " + str(art[3].likes) + "   Comments: " + str(art[3].comments) + "   Shares: " + str(art[3].shares) + "\n")
        self.FifthTitel.set("5 - " + art[4].title + "\nLikes: " + str(art[4].likes) + "   Comments: " + str(art[4].comments) + "   Shares: " + str(art[4].shares) + "\n")
        self.SixthTitel.set("6 - " + art[5].title + "\nLikes: " + str(art[5].likes) + "   Comments: " + str(art[5].comments) + "   Shares: " + str(art[5].shares) + "\n")
        self.SeventhTitel.set("7 - " + art[6].title + "\nLikes: " + str(art[6].likes) + "   Comments: " + str(art[6].comments) + "   Shares: " + str(art[6].shares) + "\n")
        self.EighthTitel.set("8 - " + art[7].title + "\nLikes: " + str(art[7].likes) + "   Comments: " + str(art[7].comments) + "   Shares: " + str(art[7].shares) + "\n")
        self.NinethTitel.set("9 - " + art[8].title + "\nLikes: " + str(art[8].likes) + "   Comments: " + str(art[8].comments) + "   Shares: " + str(art[8].shares) + "\n")
        self.TenthTitel.set("10 - " + art[9].title + "\nLikes: " + str(art[9].likes) + "   Comments: " + str(art[9].comments) + "   Shares: " + str(art[9].shares) + "\n")

    def back(self):
        self.master.switch_frame("stats")
