#import pygame,time, sys, socket #Use on Alex's machine

#import time,sys,socket #Use on Michael's machine
import tkinter as tk
#input detector


class haunts:
    def running(self):
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
            outputter(task)
        def outputter(task):
            f = open("info", "w")
            f.write(str([unit, level, task]))
            f.close()




        print("connected")
        personal = input("Ready to start?")

        if personal=="y":
            while True:
                self.calculation = ''
                self.result = ''

                self.font_header = ('Gujarati', 24)
                self.font_main = ('Gujarati', 15)
                self.button_width = 3

                self.root = tk.Tk()
                self.root.title('Haunter')
                self.root.geometry('273x200')

                self.btn_1 = tk.Button(self.root, text='Trigger', command=trigger(),
                                       width=self.button_width, font=self.font_main)
                self.btn_1.grid(row=1, column=0)


                self.root.mainloop()


        else:
            print("ERROR")






        #data handle
