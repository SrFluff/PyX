import json
from shlex import split

import kernel
import std

kernel.UID = 1
VERSION = "1.0.1"
print(f"PSH v{VERSION}")
print(f"Kernel: {kernel.NAME} v{kernel.VERSION}")

config = {
        "name":"user",
        "host":"psh"
        }

if kernel.kexists("shell.conf"):
    data = kernel.kread("shell.conf")
    try:
        config = json.loads(data)
    except Exception:
        std.error("Shell","Parsing shell.conf failed.")

while True:
    if kernel.STDERR == 0:
        a = input(f"{config['name']}@{config['host']} # ")
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
            if kernel.kread(file_name) != None:
                print(kernel.kread(file_name))
        elif com == "chid":
            if split(a)[1].isdigit():
                kernel.UID = int(split(a)[1])
            else:
                std.error("Shell","invalid character for UID.")
        elif com == "rm":
            file_name = split(a)[1]
            kernel.kremove(file_name)
    elif len(split(a)) == 3:
        com = split(a)[0]
        if com == "write":
            file_name = split(a)[1]
            kernel.kwrite(file_name,split(a)[2].replace("\\n","\n"))
        elif com == "mv":
            original_name = split(a)[1]
            new_name = split(a)[2]
            kernel.krename(original_name,new_name)
        elif com == "cp":
            original_name = split(a)[1]
            new_name = split(a)[2]
            kernel.kcopy(original_name,new_name)
    elif len(split(a)) >= 2:
        com = split(a)[0]
        if com == "rm":
            print("AAA")
            for i in split(a)[1:]:
                print(i)
                file_name = i
                kernel.kremove(file_name)
