# import pygame,time, sys, socket #Use on Alex's machine

import time, sys, socket  # Use on Michael's machine
import pygame,time, sys, socket
#input detector
unit=1
level=1

adp="poop"


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
    print("test")
    while True:
        fq = input("Press 1 for trigger, 2 for E-Stop, and 3 for reset")
        if int(fq)==2:
            E_stop()
            break
        elif int(fq)==3:
            reset()
            pq=(input ("What's the admin password?"))
            if pq==adp:
                rq=(input("Clear to reset?"))
                if rq=="y":
                    print ("reset sucessful")
                else:
                    print("Reset canceled")
            break
        else:
            print("ERROR")
else:
    print("ERROR")
