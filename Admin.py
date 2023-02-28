import pygame,time, sys, socket
#input detector
from tkinter.ttk import *
import time
import tkinter as tk
#input detector
from tkinter import Tk,Label
#haunts.trigger()


unit=1
level=1

adp="poop"

def OPS():
    print (OPS)
def E_stop():
    status = "active"
def reset():
    pq = (input("What's the admin password?"))
    if pq == adp:
        rq = (input("Clear to reset?"))
        if rq == "y":
            print("Reset sucessful")
        else:
            print("Reset canceled")
# initializing the constructor
def construction(task):
    print(unit)
    print (level)
    print (task)
    outputter(task)
def outputter(task):
    f = open("info", "w")
    f.write(str([unit, level, task]))
    f.close()


print("connected")


class haunts:
    def __init__(self):
        window = Tk()
        window.title("")
        window.geometry("600x300")
        window.configure(bg="steelblue")
        label = Label(window, text="WELCOME!", font=("Arial BLack", 78, "bold"), bg="steelblue", fg="white")
        label.pack(pady=100)
        window.update()
        time.sleep(5)
        window.destroy()
        self.root = tk.Tk()
        self.root.title('Control Point' + str(unit))
        self.root.geometry('273x200')
        self.calculation = ''
        self.result = ''
#.pack
#.grid
#.place

        self.font_header = ('Gujarati', 24)
        self.font_main = ('Gujarati', 15)
        self.button_width = 5
        self.btn_1 = tk.Button(self.root, text='Operation Status', command= OPS,
                               width=self.button_width, font=self.font_main)
        self.btn_1.grid (row=1,column=2)
        self.button_width = 8
        self.btn_2 = tk.Button(self.root, text="E_stop", command=E_stop,
                               width=self.button_width, font=self.font_main)
        self.btn_2.grid(row=2, column=1)
        self.button_width = 8
        self.btn_3 = tk.Button(self.root, text="Reset", command=reset(),
                               width=self.button_width, font=self.font_main)
        self.btn_3.grid(row=2, column=3)


        self.root.mainloop()
haunts()

