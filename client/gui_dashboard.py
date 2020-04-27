from tkinter import *
from tkinter import messagebox
import jsonpickle
from tkinter.ttk import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests
from io import BytesIO

class Dashboard(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.article_title = StringVar()
        self.article_title.set("Titel")
        self.article_text = StringVar()
        self.article_text.set("Text")
        self.Image = None
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Dashboard")
        self.master.geometry("960x618")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        self.entSearch = Entry(self, width=32, font=("arial", 16), foreground="gray")
        self.entSearch.insert(0, 'Zoek een artikel op titel')
        self.entSearch.grid(row=1, column=1, sticky=E+W, pady=(32, 32), padx=(16, 16))
        self.entSearch.bind("<FocusIn>", self.clearPlaceholder)
        self.entSearch.bind("<FocusOut>", self.addPlaceholder)


        self.btnSearch = Button(self, text="Zoek!", command=self.zoeken)
        self.btnSearch.grid(row=1, column=2, pady=(32, 32), sticky=N + S + E + W)

        self.btnStats = Button(self, text="Statistieken", command=self.zoeken)
        self.btnStats.grid(row=1, column=4, padx=(372, 16), pady=(32, 32), sticky=E)

        self.Title = Label(self, textvariable=self.article_title, font=("Arial", 24, "bold italic")).grid(row=2, column=1, columnspan=4)
        self.Text = Label(self, textvariable=self.article_text, font=("Arial",8)).grid(row=3,column=1,columnspan=4)
        #self.Image = Label(self).grid(row=4,column=1,columnspan=4, image=self.Image)

        self.btnRandom = Button(self, text="Willekeurig nieuw artikel", command=self.get_random)
        self.btnRandom.grid(row=4, column=1, padx=(16, 16), pady=(32, 32), sticky=W)

        self.get_random()

    def clearPlaceholder(self,a):
        self.entSearch.config(foreground="black")
        self.entSearch.delete(0, 'end')
    def addPlaceholder(self,a):
        self.entSearch.config(foreground="gray")
        if not self.entSearch.get():
            self.entSearch.delete(0, 'end')
            self.entSearch.insert(0, 'Zoek een artikel op titel')

    def zoeken(self):
        title = self.entSearch.get()
        print(title)
        self.master.my_writer_obj.write("title\n")
        self.master.my_writer_obj.write("%s\n" % title)
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        print(answer)
        art = jsonpickle.decode(answer)
        self.article_title.set("")
        self.article_text.set("")
        d = 1
        for i in art.title:
            if d >= 45:
                if i == " ":
                    self.article_title.set(self.article_title.get() + "\n")
                    d = 1
                else:
                    self.article_title.set(self.article_title.get() + i)
            else:
                self.article_title.set(self.article_title.get() + i)
            d += 1

        d = 1
        for i in art.text:
            if i == "\n":
                d = 1
                self.article_text.set(self.article_text.get() + i)
                continue
            else:
                if d >= 180:
                    if i == " ":
                        self.article_text.set(self.article_text.get() + "\n")
                        d = 1
                    else:
                        self.article_text.set(self.article_text.get() + i)
                else:
                    self.article_text.set(self.article_text.get() + i)
            d += 1

    def get_random(self):
        self.master.my_writer_obj.write("random\n")
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        self.article_title.set("")
        self.article_text.set("")
        d = 1
        for i in art.title:
            if d >= 45:
                if i == " ":
                    self.article_title.set(self.article_title.get() + "\n")
                    d = 1
                else:
                    self.article_title.set(self.article_title.get() + i)
            else:
                self.article_title.set(self.article_title.get() + i)
            d += 1

        d = 1
        for i in art.text:
            if i == "\n":
                d = 1
                self.article_text.set(self.article_text.get() + i)
                continue
            else:
                if d >= 180:
                    if i == " ":
                        self.article_text.set(self.article_text.get() + "\n")
                        d = 1
                    else:
                        self.article_text.set(self.article_text.get() + i)
                else:
                    self.article_text.set(self.article_text.get() + i)
            d+=1

        #sample code van img in tkinter
        #resp = requests.get(art.img)
        #load = Image.open(BytesIO(resp.content))
        #render = ImageTk.PhotoImage(load)
        #self.Image.configure(image=render)
        #self.Image.image = render