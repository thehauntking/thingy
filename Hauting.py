import pygame,time, sys, socket #Use on Alex's machine

#import time,sys,socket #Use on Michael's machine
import tkinter as tk
from tkinter.ttk import *
import time
#input detector
from tkinter import Tk,Label
#haunts.trigger()

def trigger():
    construction("trigger")


def E_stop():
    construction("E_stop")


def reset():
    construction("Reset")
    # initializing the constructor

def speak(task):
 f = open("info", "w")
 f.write(str([unit, level, task]))
 f.close()
def construction(task):
 print(unit)
 print(level)
 print(task)
 speak(task)

unit=1
level=1
def starting(self, personal,window):
  if personal=="y":
   self.root.update()
   time.sleep(5)
   self.root.destroy()
   self.root = tk.Tk()
   self.root.title('Control Point' + str(unit))
   self.root.geometry('273x200')
   self.calculation = ''
   self.result = ''
  # .pack
  # .grid
  # .place

   self.font_header = ('Gujarati', 24)
   self.text_result = tk.Text(self.root, height=1, width=16, font=self.font_header)
   self.text_result.grid(row=0, columnspan=5)
   self.font_main = ('Gujarati', 15)
   start = True
   while start == True:
     self.btn_1 = tk.Button(self.root, text='Trigger', command=trigger,
                             width=self.button_width, font=self.font_main)
     self.btn_1.grid(row=1, column=0)
   else:
      print("ERROR")


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
        self.btn_1 = tk.Button(self.root, text='trigger', command= trigger,
                               width=self.button_width, font=self.font_main)
        self.btn_1.grid (row=1,column=1)
        self.button_width = 8
        self.btn_2 = tk.Button(self.root, text="reset", command=reset,
                               width=self.button_width, font=self.font_main)
        self.btn_2.grid(row=1, column=2)
        self.button_width = 8
        self.btn_3 = tk.Button(self.root, text="E_stop", command=E_stop,
                               width=self.button_width, font=self.font_main)
        self.btn_3.grid(row=1, column=3)


        self.root.mainloop()





haunts()










        #data handle
