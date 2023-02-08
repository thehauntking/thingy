#import pygame,time, sys, socket #Use on Alex's machine

#import time,sys,socket #Use on Michael's machine
import tkinter as tk
#input detector
print("start")
#haunts.trigger()



class haunts:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Control Point(number)')
        self.root.geometry('273x200')
        self.calculation = ''
        self.result = ''
#.pack
#.grid
#.place
        self.font_header = ('Gujarati', 24)
        self.font_main = ('Gujarati', 15)
        self.button_width = 3
        self.btn_1 = tk.Button(self.root, text='Start?', command=trigger,
                               width=self.button_width, font=self.font_main)
        self.btn_2 = tk.Button(self.root, text="Don't start", command=,
                               width=self.button_width, font=self.font_main)
        self.root.mainloop()

        unit=1
        level=1
    def trigger():
        construction("trigger")
    def E_stop():
        construction("E_stop")
    def reset():
        construction("Reset")
        # initializing the constructor
    def construction(task):
        print(unit)
        print (level)
        print (task)
        speak(task)
    def speak(task):
        f = open("info", "w")
        f.write(str([unit, level, task]))
        f.close()
    def starting
        if personal=="y":
            while start True:

                self.btn_1 = tk.Button(self.root, text='Trigger', command=trigger,
                                       width=self.button_width, font=self.font_main)
                self.btn_1.grid(row=1, column=0)
        else:
            print("ERROR")

    while True:
        start = False
        starting()








        #data handle

