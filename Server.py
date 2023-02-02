unit=1
level=1

# initializing the constructor
def reset(estop):
    rest = [Unit1 [N], Unit2[N], Unit3[N]]
    f = open("All call", "w")
    f.write(str(rest))
    f.close()
    num = 0
    while estop == True:
        f = open("All call", "r")
        setting = eval(f.readline())
        f.close()
        if "N" not in setting:
            f = open("All call", "w")
            f.write(str("return"))
            f.close()
        else:
            num = num + 1
            print(num)
def construction(number, task):
    print(unit)
    print (level)
    print (task)
    if task == "trigger":
        show_outputter(number,task)
    if task == "E_stop":
        f = open("All call", "w")
        f.write(str("Estop Triggered, Unit " + str(number) + "."))
        f.close()
        estop = True
        reset(estop)
def all_outputter(number,task):
    f = open("All call", "w")
    f.write(str(task + " All, From " + number))
    f.close()
def show_outputter(number,task):
    f = open("Command", "w")
    f.write(str("midi" + str(number)))
    f.close()
print("connected")
personal = input("Ready to start?")
if personal=="y":
    while True:
        f = open("info", "r")
        command=eval(f.readline())
        print(command)
        f.close()
        input()
        number=command[0]
        task=command[2]
        construction(number, task)

else:
    print("ERROR")


#outputter

#data handle

