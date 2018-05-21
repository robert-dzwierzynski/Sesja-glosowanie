import socket
import tkinter as tk
from tkinter import Label, Button
from subprocess import Popen
import subprocess
from tkinter import messagebox

class GUI(tk.Frame):

    sub = Popen

    def __init__(self, parent,*args, **kwargs ):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()


    def build_gui(self):
        self.root.title("Sesja Gać - uruchamianie serwera")

        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=2, uniform='a')
        self.grid_columnconfigure(2, weight=3, uniform='a')
        self.grid_columnconfigure(3, weight=4, uniform='a')

        self.root.label = Label(self.root, text="Adres serwera")
        self.root.label.grid(column=0, row=1, sticky='w', columnspan=4)

        self.root.ip_add = tk.Entry(self.root)
        self.root.ip_add.insert(0,self.get_IP())
        self.root.ip_add.grid(column=1, row=2, sticky='w', columnspan=1)

        self.root.start_button = Button(self.root, text="Uruchom serwer", command=self.uruchom_serwer)
        self.root.start_button.grid(column=1, row=3, sticky='w', columnspan=1)

        self.root.close_button = Button(self.root, text="Zatrzymaj serwer", command=self.stop_serwer, state='disabled')
        self.root.close_button.grid(column=3, row=3, sticky='w', columnspan=1)


    def get_IP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return str(IP)

    def stop_serwer(self):
        state = self.root.start_button['state']
        if state == 'disabled':
            Popen("taskkill /F /T /PID %i"%self.sub.pid, shell=True)
            self.root.start_button.config(state='active')
            self.root.ip_add.config(state='normal')
            self.root.close_button.config(state='disabled')



    def uruchom_serwer(self):
        cmd = 'python C:/Sesja/manage.py runserver '+self.root.ip_add.get()+':80'
        self.sub = Popen(cmd, shell=True)
        self.root.start_button.config(state='disabled')
        self.root.ip_add.config(state='disabled')
        self.root.close_button.config(state='active')



root = tk.Tk()

my_gui = GUI(root)

def on_closing():
    if messagebox.askokcancel("Zamykanie", "Czy napewno chcesz zamknąć?"):
        my_gui.stop_serwer()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

