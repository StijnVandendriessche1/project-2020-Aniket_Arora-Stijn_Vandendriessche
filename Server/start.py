from tkinter import *
import sys

from Server.gui_server import ServerWindow


def callback():
    print("callback")
    gui_server.afsluiten_server()
    root.destroy()


root = Tk()
root.geometry("1280x720")
gui_server = ServerWindow(root)
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()