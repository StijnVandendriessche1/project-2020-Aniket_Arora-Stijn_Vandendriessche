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
        self.lstnumbers = None
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

        self.btnStats = Button(self, text="Statistieken", command=self.switch_stats)
        self.btnStats.grid(row=1, column=4, padx=(350, 16), pady=(32, 32), sticky=E)

        self.Title = Label(self, textvariable=self.article_title, font=("Arial", 24, "bold italic")).grid(row=2, column=1, columnspan=4)

        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.lstnumbers = Listbox(self, yscrollcommand=self.scrollbar.set, height=20)
        self.scrollbar.config(command=self.lstnumbers.yview)

        self.lstnumbers.grid(row=3, column=1, columnspan=4, sticky=N + S + E + W)
        self.scrollbar.grid(row=3, column=5, sticky=N + S)

        #self.Text = Label(self, textvariable=self.article_text, font=("Arial",8)).grid(row=4,column=1,columnspan=4)
        #self.Image = Label(self).grid(row=4,column=1,columnspan=4, image=self.Image)

        self.btnRandom = Button(self, text="Willekeurig nieuw artikel", command=self.get_random)
        self.btnRandom.grid(row=5, column=1, padx=(16, 16), pady=(32, 32), sticky=W)

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
        self.master.my_writer_obj.write("title\n")
        self.master.my_writer_obj.write("%s\n" % title)
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        self.lstnumbers.delete(0, 'end')
        self.article_title.set("")
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
        a = ""
        b = 0
        for i in art.text:
            if i == "\n":
                self.lstnumbers.insert(b, a)
                a = ""
                b += 2
                d = 1
                continue
            else:
                if d >= 150:
                    if i == " ":
                        self.lstnumbers.insert(b, a)
                        a = ""
                        b += 1
                        d = 1
                    else:
                        a += i
                else:
                    a += i
            d += 1

    def get_random(self):
        self.master.my_writer_obj.write("random\n")
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        self.lstnumbers.delete(0,'end')
        self.article_title.set("")
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
        a = ""
        b = 0
        for i in art.text:
            if i == "\n":
                self.lstnumbers.insert(b,a)
                a = ""
                b += 2
                d = 1
                continue
            else:
                if d >= 150:
                    if i == " ":
                        self.lstnumbers.insert(b, a)
                        a = ""
                        b +=1
                        d = 1
                    else:
                        a += i
                else:
                    a += i
            d+=1

        #sample code van img in tkinter
        #resp = requests.get(art.img)
        #load = Image.open(BytesIO(resp.content))
        #render = ImageTk.PhotoImage(load)
        #self.Image.configure(image=render)
        #self.Image.image = render

    def switch_stats(self):
        self.master.switch_frame("stats")