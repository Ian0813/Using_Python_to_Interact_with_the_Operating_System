#!/usr/bin/python3.7


import sys
import subprocess


with open(sys.argv[1], "r+") as f:
    name = f.read()
    name = name.split('/')
    for i in range(len(name)):
        temp = name[i].strip()
        temp = temp.replace("..", "")
        print(temp)
        if "jane" in temp:
            temp2 = temp.replace("jane", "jdoe")
            #print(temp)
            #print(temp2)
            subprocess.run(['mv', "../data/" +  temp, "../data/" + temp2])

