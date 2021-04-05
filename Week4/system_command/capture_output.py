#!/usr/bin/python3.7

import subprocess

result = subprocess.run(["host", "8.8.8.8.8"], capture_output=True)

if not result.returncode == 0:
    print("Test")

print(result.returncode) # return the status code of an executed command

print(result.stdout) # show the output of a command in bytes

print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)

print(result.returncode)

print(result.stdout)

print(result.stderr)
