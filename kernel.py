import file

UID = 1
STDERR = 0
VERSION = "1.0.1"
NAME = "PyX Kernel"
TRUSTED = []

def kerror(error_message,error_code=1):
    global STDERR
    print(f"Kernel: Error, {error_message}")
    STDERR = error_code

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
        return data[file_name]

def kexists(file_name):
    return file_name in file.rraw()

def kremove(file_name):
    if UID == 0 or UID in TRUSTED:
        if not kexists(file_name):
            kerror(f"'{file_name}' no such file.")
        else:
            file.remove(file_name)
    else:
        kerror("UID is not allowed to write.")

def krename(original_name,new_name):
    if UID == 0 or UID in TRUSTED:
        if not kexists(original_name):
            kerror(f"'{original_name}' no such file.")
        elif kexists(new_name):
            kerror(f"'{new_name}' exists.")
        else:
            file.rename(original_name,new_name)
    else:
        kerror("UID is not allowed to write.")

def kcopy(original_name, new_name):
    if UID == 0 or UID in TRUSTED:
        if not kexists(original_name):
            kerror(f"'{original_name}' no such file.")
        elif kexists(new_name):
            kerror(f"'{new_name}' exists.")
        else:
            file.copy(original_name,new_name)
    else:
        kerror("UID is not allowed to write.")
