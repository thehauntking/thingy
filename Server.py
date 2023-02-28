unit="Z"
level=10
import time
# initializing the constructor
def reset(estop):
    rest = ["Unit1 [N]", "Unit2[N]", "Unit3[N]"]
    f = open("All call", "w")
    f.write(str(rest))
    f.close()
    num = 0
    while estop == True:
        f = open("All call", "r")
        setting = (f.readline())
        f.close()
        if "N" not in setting:
            f = open("All call", "w")
            f.write(str("return"))
            f.close()
        else:
            time.sleep(0)
            num = num + 1
            if num==60:
                break

def construction(number, task):
    #print(unit)
    #print (level)
    #print (task)
    if task == "trigger":
        show_outputter(number,1)
    if task == "E_stop":
        show_outputter(number, 2)
        f = open("All call", "w")
        f.write(str("Estop Triggered, Unit " + str(number) + "."))
        f.close()
        f = open("Status", "w")
        f.write(str("Estop Triggered, Unit " + str(number) + "."))
        f.close()
        estop = True
        reset(estop)
def all_outputter(number,task):
    f = open("All call", "w")
    f.write(str(task + " All, From " + number))
    f.close()
def show_outputter(number,task):
    f = open("Show command", "w")
    f.write(str("midi" + str(number)))
    f.close()
print("connected")
personal = input("Ready to start?")
ocommand = []
if personal=="y":
    while True:
        f = open("info", "r")
        ncommand=eval(f.readline())
        print(ncommand)
        f.close()
        input()
        if ncommand == ocommand:
            print("Np")
        else:
            command = ncommand
            ocommand = command
            number=command[0]
            task=command[2]
            construction(number, task)

else:
    print("ERROR")


#outputter

#data handle

