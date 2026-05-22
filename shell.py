import kernel
import std

from shlex import split

kernel.UID = 1
while True:
    if kernel.STDERR == 0:
        a = input("> ")
    else:
        a = input(f"[{kernel.STDERR}]> ")
    kernel.STDERR = 0
    if a == "exit":
        break
    elif a == "uid":
        print(kernel.UID)
    elif a == "ls":
        for i in kernel.file.rraw():
            print(i,end=" ")
        print()
    elif a == "clear":
        kernel.file.os.system("clear")
    elif len(split(a)) == 2:
        com = split(a)[0]
        if com == "touch":
            file_name = split(a)[1]
            kernel.kwrite(file_name,"")
        elif com == "cat":
            file_name = split(a)[1]
            kernel.kread(file_name)
        elif com == "chid":
            if split(a)[1].isdigit():
                kernel.UID = int(split(a)[1])
            else:
                std.error("Shell","invalid character for UID.")
    elif len(split(a)) == 3:
        com = split(a)[0]
        if com == "write":
            file_name = split(a)[1]
            kernel.kwrite(file_name,split(a)[2])
    elif len(split(a)) >= 2:
        com = split(a)[0]
        if com == "rm":
            for i in split(a)[1:]:
                file_name = i
                kernel.kremove(file_name)
