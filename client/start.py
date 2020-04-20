from tkinter import *

from client.gui_client import  Window

def callback():
    print("callback")
    gui_client.close_connection()
    root.destroy()

root = Tk()
root.geometry("600x500")
gui_client = Window(root)
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()