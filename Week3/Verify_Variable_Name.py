#!/usr/bin/python3
import sys
import re

pattern = "^[a-zA-Z_][a-zA-Z0-9_]*$" # The rule of variable name

var = sys.argv[1]

print("The variable name : " + var)
if(re.search(pattern, var)):
    print("Is valid.")
else:
    print("Is invalid.")


