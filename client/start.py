from tkinter import *
from client.gui_client import Window
from client.gui_dashboard import Dashboard
import logging
import socket
from tkinter import messagebox

class StartApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.my_writer_obj = None
        self.socket_to_server = None
        self.makeConnnectionWithServer()
        self.switch_frame("start")

    def __del__(self):
        self.close_connection()

    def makeConnnectionWithServer(self):
        try:
            logging.info("Making connection with server...")
            # get local machine name
            host = socket.gethostname()
            port = 9999
            self.socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connection to hostname on the port.
            self.socket_to_server.connect((host, port))
            self.my_writer_obj = self.socket_to_server.makefile(mode='rw')
            logging.info("Open connection with server succesfully")
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)

    def close_connection(self):
        try:
            logging.info("Close connection with server...")
            self.my_writer_obj.write("%s\n" % "CLOSE")
            self.my_writer_obj.flush()
            self.socket_to_server.close()
        except Exception as ex:
            logging.error("Foutmelding: %s" % ex)
            messagebox.showinfo("Sommen", "Something has gone wrong...")

    #we switchen tss 3 frames: startframe <> bmiframe, startframe <> numbersframe

    def switch_frame(self, name_class):
        """Destroys current frame and replaces it with a new one."""
        if self._frame is not None:
            self._frame.destroy()

        if name_class == "start":
            new_frame = Window(self)
        elif name_class == "dashboard":
            new_frame = Dashboard(self)
        #elif name_class == "numbers":
            #new_frame = NumbersFrame(self)

        if new_frame is not None:
            self._frame = new_frame
            self._frame.pack()

root = StartApp()
root.mainloop()