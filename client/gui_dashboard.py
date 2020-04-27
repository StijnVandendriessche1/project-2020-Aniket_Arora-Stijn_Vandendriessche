from tkinter import *
from tkinter import messagebox
import jsonpickle
from tkinter.ttk import *

class Dashboard(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)
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

        #Label(self, text="Zoeken:", font=("Helvetica", 32, "bold italic")).grid(row=0)

        self.zoeken()

    def clearPlaceholder(self,a):
        self.entSearch.config(foreground="black")
        self.entSearch.delete(0, 'end')
    def addPlaceholder(self,a):
        self.entSearch.config(foreground="gray")
        self.entSearch.delete(0, 'end')
        self.entSearch.insert(0, 'Zoek een artikel op titel')

    def zoeken(self, title="Mikhail Saakashvili quits as Odessa governor"):
        self.master.my_writer_obj.write("title\n")
        self.master.my_writer_obj.write("%s\n" % title)
        self.master.my_writer_obj.flush()
        answer = self.master.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        print(art.img)

        # sample code van img in tkinter
        # resp = requests.get(art.img)
        # load = Image.open(BytesIO(resp.content))
        # render = ImageTk.PhotoImage(load)
        # img = Label(image=render)
        # img.image = render
        # img.place(x=0,y=0)