#! /usr/bin/python3

import re
import os

def check_web_address(text):

  pattern = "[a-zA-Z\_\-\.\+]*\.[a-zA-Z]*$"

  result = re.search(pattern, text)

  return result != None



print(check_web_address("gmail.com")) # True

print(check_web_address("www@google")) # False

print(check_web_address("www.Coursera.org")) # True

print(check_web_address("web-address.com/homepage")) # False

print(check_web_address("My_Favorite-Blog.US")) # True

file = os.popen("find . -iname '*.py'")
reader = file.read()
print(reader)
