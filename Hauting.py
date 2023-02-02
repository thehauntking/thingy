import pygame,time, sys, socket
#input detector


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
        from tkinter import *
        master = Tk()
        button = Button(master, text='E_stop', command=E_stop())
        button2 = Button(master, text='reset', command=reset())
        button.pack()
        button2.pack()
        mainloop()

else:
    print("ERROR")






#data handle
