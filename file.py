import os
import json

def new():
    if not os.path.exists("file.json"):
        with open("file.json","w") as f:
            f.write(json.dumps({}))
            f.close()
        return 0
    return 1

def rraw():
    new()
    with open("file.json","r") as f:
        ret = json.loads(f.read())
        f.close()
    return ret

def wraw(raw_dict: dict):
    with open("file.json","w") as f:
        f.write(json.dumps(raw_dict))
        f.close()
    return 0

def write(file_name: str,file_content: str):
    new()
    data = rraw()
    data[file_name] = file_content
    wraw(data)
    return 0

def remove(file_name):
    data = rraw()
    if file_name not in data:
        return 1
    data.pop(file_name)
    wraw(data)
    return 0

def copy(original_name, new_name):
    data = rraw()
    if original_name not in data:
        return 1
    data[new_name] = data[original_name]
    wraw(data)
    return 0

def rename(original_name, new_name):
    data = rraw()
    if original_name not in data or new_name in data:
        return 1
    copy(original_name,new_name)
    remove(original_name)
    return 0
