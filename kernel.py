import file

UID = 1
STDERR = 0
VERSION = "1.0.0"
TRUSTED = []

def kerror(error_message,error_code=1):
    global STDERR
    print(f"Kernel: Error, {error_message}")
    STDERR = error_code

def kinfo():
    print("Python kernel")
    print(f"Version {VERSION}")
    print("Created and maintained by SrFluff")

def kwrite(file_name, file_content):
    if UID == 0 or UID in TRUSTED:
        file.write(file_name,file_content)
    else:
        kerror("UID is not allowed to write.")

def kread(file_name):
    data = file.rraw()
    if file_name not in data:
        kerror("No such file.")
    else:
        print(data[file_name])

def kremove(file_name):
    if UID == 0 or UID in TRUSTED:
        if file.remove(file_name) == 1:
            kerror("No such file.")
    else:
        kerror("UID is not allowed to write.")
