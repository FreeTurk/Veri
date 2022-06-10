from asyncore import read
from genericpath import exists
import time


class Veri:
    global exists
    global found
    global readtype

    def create(filename, content, type, name):
        exists = False
        time_now = int(time.time())
        f = open(filename, "r+")
        for line in f:
            if name in line:
                print("Veri Warning: {} already exists, did not create".format(name))
                exists = True
                break
        if type == "str" and exists == False:
            content = '"' + content + '"'
            f.write("dec {}: (\ntype: {};;\ncreated: {};;\nlast: {};;\ndata: {};;\n)\n".format(
                name, type, time_now, time_now, content))
        elif type != "str" and exists == False:
            f.write("dec {}: (\ntype: {};;\ncreated: {};;\nlast: {};;\ndata: {};;\n)\n".format(
                name, type, time_now, time_now, content))

    class read():
        def content(filename, name):
            found = False
            readtype = ""
            f = open(filename, "r")
            content = ""
            for line in f:
                if name in line and found != True:
                    found = True
                if line.startswith("data:") and found == True:
                    content = line.split("data:")[
                        1].strip().strip(";;").strip('"')
                    break
                if line.startswith("type:") and found == True:
                    readtype = line.split("type:")[1].strip().strip(";;")
            if readtype == "str":
                return str(content)
            elif readtype == "int":
                return int(content)
            elif readtype == "flt" or readtype == "tme":
                return float(content)

        def type(filename, name):
            found = False
            readtype = ""
            f = open(filename, "r")
            for line in f:
                if name in line and found != True:
                    found = True
                if line.startswith("type:") and found == True:
                    readtype = line.split("type:")[1].strip().strip(";;")
                    break
            return readtype
