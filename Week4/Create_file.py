#!/usr/bin/python3.7
import os
import sys
import subprocess

filename=sys.argv[1]
if not os.path.exists(filename):
    with open(filename, "w") as f:
        if sys.argv[2] == "py":
            subprocess.run(["touch", filename])
            result = subprocess.run(["which", "python3.7"], capture_output=True)
            print(result.returncode)
            f.write("#!" + result.stdout.decode())
            print("Create " + filename)
            #print(type(filename))
        else:
            print("Write to a new file")
            f.write(input())
else:
    print("Error, the file {} already exists!". format(filename))
    sys.exit(1)
