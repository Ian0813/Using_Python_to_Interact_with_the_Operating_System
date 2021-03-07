#!/usr/bin/python3.7

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/google/chrome", my_env["PATH"]])

result = subprocess.run(["google-chrome"], env=my_env)
