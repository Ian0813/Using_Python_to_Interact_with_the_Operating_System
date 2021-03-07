#!/usr/bin/python3
import re
# the first parameter is a regular expression pattern, the front of word r represent that is a raw string.
result = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(result)
