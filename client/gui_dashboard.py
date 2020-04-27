from tkinter import *
from tkinter import messagebox
import jsonpickle

class Dashboard(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Dashboard")
        self.master.geometry("960x675")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        self.entSearch = Entry(self, width=16, font=("arial", 32))
        self.entSearch.grid(row=1, column=1, sticky=E+W, pady=32, padx=16)

        self.btnSearch = Button(self, text="Zoeken", command=self.zoeken)
        self.btnSearch.grid(row=2, column=0, columnspan=3, pady=(0, 5), padx=(5, 5), sticky=N + S + E + W)

        #Label(self, text="Zoeken:", font=("Helvetica", 32, "bold italic")).grid(row=0)

        self.zoeken()

    def zoeken(self, title="Mikhail Saakashvili quits as Odessa governor"):
        StartApp.my_writer_obj.write("title\n")
        StartApp.my_writer_obj.write("%s\n" % title)
        StartApp.my_writer_obj.flush()
        answer = StartApp.my_writer_obj.readline().rstrip('\n')
        art = jsonpickle.decode(answer)
        print(art.img)

        # sample code van img in tkinter
        # resp = requests.get(art.img)
        # load = Image.open(BytesIO(resp.content))
        # render = ImageTk.PhotoImage(load)
        # img = Label(image=render)
        # img.image = render
        # img.place(x=0,y=0)