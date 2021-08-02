import os
import json


def read_data():
    if not os.path.exists("./data.txt"):
        with open("./data.txt", "w") as _f:
            json.dump([], _f)
        return []
    
    with open("./data.txt", "r") as _f:
        res=json.load(_f)

    return res


def write_data(record):
    if not os.path.exists("./data.txt"):
        with open("./data.txt", "w") as _f:
            json.dump([record], _f)
        return
    
    data = read_data()
    data.append(record)
    with open("./data.txt", "w") as _f:
            json.dump(data, _f)