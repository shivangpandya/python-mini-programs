# Program to find all phone numbers in a paragraph using regex

import re

print('Copy the message you want to enter and we will find out the phone number from it')
message=input()
phoneRegex = re.compile(message)
mo = phoneRegex.findall(message)
mo.group()
